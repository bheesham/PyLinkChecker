# Copyright (C) 2011 Bheesham Persaud
# The license is available in LICENSE
from __future__ import division
import re

from includes.functions import *

class fileserve_com:
	def init( self ):
		self.url_pattern = re.compile( r'(http://www\.fileserve\.com/file/([A-Za-z0-9]+))', re.I )
		self.result_pattern = re.compile( r'<td>(http://www\.fileserve\.com/file/([A-Za-z0-9]+))</td><td>--</td>', re.I )
		self.url = 'www.fileserve.com'
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
			params = urllib.urlencode({ 'urls': files_joined, 'submit': ' Check Urls ' })
			browser = urllib.urlopen( "http://fileserve.com/link-checker.php", params )
			res_urls = browser.read()
			res_urls = res_urls.replace( "\r", '' )
			res_urls = res_urls.replace( "\n", '' )
			res_urls = res_urls.replace( " ", '' )
			res_urls = self.result_pattern.findall( res_urls )
			for res_url in res_urls:
				dead.append( res_url[0] )
				files_list.remove( res_url[0] )
		return [ self.url, files_list, dead ]