# Copyright (C) 2011 Bheesham Persaud
# The license is available in LICENSE
from linkchecker import *


# NOTE: filesonic is a little girl

linkchecker = linkchecker()

links = " https://rapidshare.com/files/1754580889/smbc_save_data_sophia.txt "

parsed_links = []
parsed_links = linkchecker.parse( links )
result = linkchecker.check( parsed_links )

total = len( parsed_links )
total_alive = 0
total_dead = 0

for host, alive_urls, dead_urls in result:
	print "For host: {0}".format( host )
	print "  Alive: {0}".format( len( alive_urls ) )
	print "  Dead: {0}".format( len( dead_urls ) )