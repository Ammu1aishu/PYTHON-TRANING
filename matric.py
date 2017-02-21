class matrix3x3:
	def __init__(self,m):
		matrix = []
		self.m = [ [ m[i][j] for j in range(3) ] for i in range(3) ]
		row = []
		data = input('enter the values:')
		row.append(data)
		matrix.append(data)
mat = matrix3x3(3)
print(mat.m)
