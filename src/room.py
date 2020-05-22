# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
	def __init__( self, name, desc):
		self.name = name
		self.desc = desc

	def __str__( self):
		return f"{self.name}"

	def printDescription( self):
		return f"{self.desc}"