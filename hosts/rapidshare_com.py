# Copyright (C) 2011 Bheesham Persaud
# The license is available in LICENSE
from __future__ import division
import re

from includes.functions import *

class rapidshare_com:
	def init( self ):
		self.url_pattern = re.compile( r'(http:\/\/rapidshare\.com\/files\/([0-9]+)/([A-Za-z0-9_\-\.]+))', re.I )
		self.result_pattern = re.compile( r'([0-9]+),([A-Za-z0-9_\-\.]+),0,0,0,0,0', re.I )
		self.url = 'rapidshare.com'
		return None
	def parse( self, text ):
		matches = self.url_pattern.findall( text )
		result_urls = []
		if len( matches ) > 0:
			for url in matches:
				result_urls.append( url[0] )
			return result_urls
		else:
			return None
	def check( self, files_list ):
		dead = []
		files_split = split_list( files_list, 50 )
		for files in files_split:
			ids = []
			names = []
			for file in files:
				file_info = self.url_pattern.findall( file )
				try:
					ids.append( file_info[0][1] )
					names.append( file_info[0][2] )
				except IndexError:
					pass
			ids = ",".join( ids )
			names = ",".join( names )
			url = "https://api.rapidshare.com/cgi-bin/rsapi.cgi?sub=checkfiles&files={0}&filenames={1}".format( ids, names )
			browser = urllib.urlopen( url )
			res_urls = browser.read()
			res_urls = self.result_pattern.findall( res_urls )
			for res_url in res_urls:
				dead_url = "http://rapidshare.com/files/{0}/{1}".format( res_url[0], res_url[1] )
				dead.append( dead_url )
				files_list.remove( dead_url )
		return [ self.url, files_list, dead ]