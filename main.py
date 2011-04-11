from includes.database import *
from includes.functions import *


from hosts.hotfile_com import *
from hosts.fileserve_com import *

# fileserve X
# filesonic
# hotfile X
# uploadstation

hotfile_com = hotfile_com()
fileserve_com = fileserve_com()

# example:
if fileserve_com.parse( "http://www.fileserve.com/file/sSNFHtjD http://www.fileserve.com/file/czfGCd4 http://www.fileserve.com/file/sTZxpYK" ) == 1:
	ratio = fileserve_com.check()
	if ratio == 1:
		print "there are no dead links"
	else:
		print ratio
else:
	print "meh"