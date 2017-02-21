class area:
	def __init__(self,l,b):
		self.l = l
		self.b = b
		#print "enter the length & breath"
	def str(self):
		return self.l * self.b		
#a1 = area (12,5)
#print a1.str()
a1 = input('enter first values:')
c1 = input('enter second value:')
b1 = area(a1,c1)
print b1.str()
