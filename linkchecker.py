# Copyright (C) 2011 Bheesham Persaud
# The license is available in LICENSE
from __future__ import division
import re
import gc
from types import *

from includes.functions import *
from hosts.rapidshare_com import *
from hosts.hotfile_com import *
from hosts.fileserve_com import *
from hosts.wupload_com import *
from hosts.oron_com import *

class linkchecker:
	def __init__( self ):
		"""Initialize the link checker. This will load all of the hosts, and compile all of the regular expressions"""
		self.hosts = []
		self.host_urls = []
		self.patterns = []
		self.hosts.append( rapidshare_com() )
		self.hosts.append( hotfile_com() )
		self.hosts.append( fileserve_com() )
		self.hosts.append( wupload_com() )
		self.hosts.append( oron_com() )
		
		# after all of the sites are loaded into that array
		# start compiling the regex!
		for host in self.hosts:
			host.init()
			self.host_urls.append( host.url )
		gc.collect()
		return None
	def parse( self, text ):
		"""Parses the text and returns a list of links."""
		links = []
		result = []
		for host in self.hosts:
			links = host.parse( text )
			found_links = []			
			try:
				if len( links ) > 0:
					for link in links:
						found_links.append( link )
					found_links =  unique( found_links )
			except TypeError:
				pass
			result.append( [ host.url, found_links ] )
		return result
	def check( self, files ):
		"""Will first check to see if the text is parsed, then check the links."""
		if type( files ) is not ListType:
			files = self.parse( files )
		result = []
		t_result = []
		index = 0
		for host, file in files:
			index = self.host_urls.index( host )
			t_result = self.hosts[index].check( file )
			result.append( t_result )
		return result