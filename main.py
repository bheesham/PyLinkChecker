# Copyright (C) 2011 Bheesham Persaud
# The license is available in LICENSE
from linkchecker import *


# NOTE: filesonic is a little girl

linkchecker = linkchecker()

links = ""

links += " http://www.wupload.com/file/59331596/MyGBackup.F3-skr.part1.rar "
links += " http://www.wupload.com/file/59331948/MyGBackup.F3-skr.part2.rar "
links += " http://www.wupload.com/file/59331936/MyGBackup.F3-skr.part3.rar "
links += " http://www.wupload.com/file/59330906/MyGBackup.F3-skr.part4.rar "
links += " http://www.wupload.com/file/59282205/MyGBackup.F3-skr_update1.rar "
links += " http://www.wupload.com/file/4170892 "

links += " http://www.easy-share.com/1916731918/Yars.Revenge.part1.rar "
links += " http://www.easy-share.com/1916731954 "
links += " http://www.easy-share.com/1916731942 "
links += " http://www.easy-share.com/1916731923 "
links += " http://www.easy-share.com/1916731822 "
links += " http://www.easy-share.com/1916731824 "
links += " http://www.easy-share.com/1916731825 "
links += " http://www.easy-share.com/1916731826 "
links += " http://www.easy-share.com/1916731827 "
links += " http://www.easy-share.com/1916731828 "
links += " http://www.easy-share.com/1916731832 "
links += " http://www.easy-share.com/1916731817 "

links += " http://oron.com/0jxyfnhfjzjk/Adobe_CS5_Complete_Licensing_Solution.rar.html "
links += " http://oron.com/kshgkyg9gyii/Adobe.Photoshop.Lightroom.v2.6.1.639867.Multilingual.Incl.Keymaker-CORE.rar.html "
links += " http://oron.com/4815anlteu23/Adobe.Creative.Suite.5.Master.Collection.Multilingual.ESD.ISO-CORE.part10.rar.html "
links += " http://oron.com/m0ofajp0thlz/Adobe.CS5.Master.Collection.RETAIL.READNFO-ISO.part30.rar.html "


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