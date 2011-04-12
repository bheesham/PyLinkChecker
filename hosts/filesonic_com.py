from __future__ import division
import re

from includes.functions import *

class filesonic_com:
	def parse( self, text ):
		self.url_pattern = re.compile( r'(http://www.filesonic.com/file/(\d+)/([A-Za-z0-9\-_\.]+))', re.I )
		self.url_res_pattern = re.compile( r'<p>(\d+) / (\d+) Available</p>', re.I )
		matches = self.url_pattern.findall( text )
		self.check_urls = []
		if len( matches ) > 0:
			for url in matches:
				self.check_urls.append( url[0] )
			return 1
		else:
			return None
	def check( self ):
		files = "\r".join( self.check_urls )
		params = urllib.urlencode({ 'redirect': '', 'links': files })
		browser = urllib.urlopen( "http://www.filesonic.com/link-checker", params )
		res_urls = browser.read()
		res_urls = self.url_res_pattern.findall( res_urls )
		if len( res_urls ) == 1:
			ratio = ( int( res_urls[0][0] ) / int( res_urls[0][1] ) )
			return ratio
		else:
			return 0
