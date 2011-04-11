from __future__ import division
import re

from includes.functions import *

class hotfile_com:
	def parse( self, text ):
		self.url_pattern = re.compile( r'(http:\/\/hotfile.com\/dl\/([0-9]+)/([A-Za-z0-9]+)/([A-Za-z0-9\-_\.]+)\.html)', re.I )
		self.url_res_pattern = re.compile( r'href="(http:\/\/hotfile.com\/dl\/([0-9]+)/([A-Za-z0-9]+)/([A-Za-z0-9\-_\.]+)\.html)">', re.I )
		matches = self.url_pattern.findall( text )
		self.check_urls = []
		if len( matches ) > 0:
			for url in matches:
				self.check_urls.append( url[0] )
			return 1
		else:
			return None
	def check( self ):
		files = "\r\n".join( self.check_urls )
		params = urllib.urlencode({ 'files': files, 'submit': ' Check Urls ' })
		browser = urllib.urlopen( "http://hotfile.com/checkfiles.html", params )
		res_urls = browser.read()
		res_urls = self.url_res_pattern.findall( res_urls )
		if len( res_urls ) == len( self.check_urls ):
			return 1
		else:
			ratio = ( len( res_urls ) / len( self.check_urls ) )
			return ratio