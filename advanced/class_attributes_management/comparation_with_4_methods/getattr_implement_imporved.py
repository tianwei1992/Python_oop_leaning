class Powers():
	def __init__(self, square_base, cube_base):
		self._square_base = square_base
		self._cube_base = cube_base
	def __getattr__(self, item):
		if item == "square":
			return self._square_base ** 2
		elif item == "cube":
			return self._cube_base ** 3
		else:
			raise TypeError("UnDefined")

	def __setattr__(self, key, value):
		if key == "square":
			key = "_square_base"
		elif key == "cube":
			key = "_cube_base"
		self.__dict__[key] = value


X = Powers(3, 4)
print(X.square) # 3 ** 2 = 9
print(X.cube) # 4 ** 3 = 64
X.square = 5
print(X.square) # 5 ** 2 = 25
X.name = "x"
print(X.name)

