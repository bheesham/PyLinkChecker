from includes.database import *
from includes.functions import *


from hosts.fileserve_com import *
from hosts.hotfile_com import *
from hosts.filesonic_com import *

# fileserve X
# filesonic
# hotfile X

hotfile_com = hotfile_com()
fileserve_com = fileserve_com()
filesonic_com = filesonic_com()

# example:
if filesonic_com.parse( "http://www.filesonic.com/file/251557719/Available.zip" ) == 1:
	ratio = filesonic_com.check()
	if ratio == 1:
		print "there are no dead links"
	else:
		print ratio
else:
	print "meh"