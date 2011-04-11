from __future__ import division
import re

from includes.functions import *

class fileserve_com:
	def parse( self, text ):
		self.url_pattern = re.compile( r'(http://www.fileserve.com/file/([A-Za-z0-9]+))', re.I )
		self.url_res_pattern = re.compile( r'<td>(http://www.fileserve.com/file/([A-Za-z0-9]+))</td><td>--</td>', re.I )
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
		params = urllib.urlencode({ 'urls': files, 'submit': 'Check Urls' })
		browser = urllib.urlopen( "http://fileserve.com/link-checker.php", params )
		res_urls = browser.read()
		res_urls = res_urls.replace( "\r", '' )
		res_urls = res_urls.replace( "\n", '' )
		res_urls = res_urls.replace( " ", '' )
		res_urls = self.url_res_pattern.findall( res_urls )
		if len( res_urls ) == 0:
			return 1
		else:
			ratio = len( self.check_urls ) - len( res_urls )
			ratio = ( ratio / len( self.check_urls ) )
			return ratio