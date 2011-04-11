from __future__ import division
import re

from includes.functions import *

class uploadstation_com:
	def parse( self, text ):
		self.url_pattern = re.compile( r'(http://www.uploadstation.com/file/([A-Za-z0-9]+))', re.I )
		self.url_res_pattern = re.compile( r'<div class="col col1">(http://www.uploadstation.com/file/([A-Za-z0-9]+))</div><div class="col col2">--</div>', re.I )
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
		params = urllib.urlencode({ 'urls': files })
		browser = urllib.urlopen( "http://www.uploadstation.com/link-checker.php", params )
		res_urls = browser.read()
		f = open( 'meh', 'w' )
		f.write( res_urls )
		f.close()
		res_urls = self.url_res_pattern.findall( res_urls )
		if len( res_urls ) == 0:
			return 1
		else:
			ratio = len( self.check_urls ) - len( res_urls )
			ratio = ( ratio / len( self.check_urls ) )
			return ratio