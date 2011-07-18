# Copyright (C) 2011 Bheesham Persaud
# The license is available in LICENSE
import urllib, httplib
from itertools import izip_longest

# change the user agent
class AppURLopener( urllib.FancyURLopener ):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.98 Safari/534.13' # google chrome
urllib._urlopener = AppURLopener()

def unique(seq, idfun=None):
    # order preserving 
    if idfun is None: 
        def idfun(x): return x 
    seen = {} 
    result = [] 
    for item in seq: 
        marker = idfun(item) 
        # in old Python versions: 
        # if seen.has_key(marker) 
        # but in new ones: 
        if marker in seen: continue 
        seen[marker] = 1 
        result.append(item) 
    return result

def split_list( iterable, n, padvalue="" ):
    """grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x') -- J.F. Sebastian"""
    return izip_longest( *[iter( iterable )]*n, fillvalue=padvalue )