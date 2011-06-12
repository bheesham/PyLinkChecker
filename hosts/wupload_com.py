# Copyright (C) 2011 Bheesham Persaud
# The license is available in LICENSE
from __future__ import division
import re

from includes.functions import *

class wupload_com:
	def init( self ):
		self.url_pattern = re.compile( r'(http:\/\/www\.wupload\.com\/file\/([0-9]+)/([A-Za-z0-9_\-\.]+))', re.I )
		self.result_pattern = re.compile( r'(http:\/\/www\.wupload\.com\/file\/([0-9]+)/([A-Za-z0-9_\-\.]+))</span></td><tdclass="fileName"><span>-', re.I )
		self.url = 'www.wupload.com'
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
			files_joined = "\r\n".join( files )
			params = urllib.urlencode({ 'redirect': '/', 'links': files_joined })
			browser = urllib.urlopen( "http://www.wupload.com/link-checker", params )
			res_urls = browser.read()
			res_urls = res_urls.replace( "\r", '' )
			res_urls = res_urls.replace( "\n", '' )
			res_urls = res_urls.replace( " ", '' )
			res_urls = self.result_pattern.findall( res_urls )
			for res_url in res_urls:
				dead.append( res_url[0] )
				files_list.remove( res_url[0] )
		return [ self.url, files_list, dead ]