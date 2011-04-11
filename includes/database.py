import MySQLdb

class database:
	def connect( self, host, user, passw, name ):
		con = MySQLdb.connect( host, user, passw, name )
		return con