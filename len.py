class area:
	def __init__(self,l,b):
		self.l = l
		self.b = b
		#print "enter the length & breath"
	def str(self):
		return self.l * self.b		
a1 = area (12,5)
print a1.str()
