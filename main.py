from includes.database import *
from includes.functions import *


from hosts.fileserve_com import *
from hosts.hotfile_com import *
from hosts.uploadstation_com import *

# fileserve X
# filesonic
# hotfile X
# uploadstation

hotfile_com = hotfile_com()
fileserve_com = fileserve_com()
uploadstation_com = uploadstation_com()

# example:
if uploadstation_com.parse( "http://www.uploadstation.com/file/kXJhdWg/phpBB-2.0.23.zip" ) == 1:
	ratio = uploadstation_com.check()
	if ratio == 1:
		print "there are no dead links"
	else:
		print ratio
else:
	print "meh"