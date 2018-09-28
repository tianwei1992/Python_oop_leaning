class Powers():
	def __init__(self, square_base, cube_base):

		self._square_base = square_base
		self._cube_base = cube_base
	def __getattribute__(self, item):
		if item == "square":
			attr = "_square_base"
			return object.__getattribute__(self, attr) ** 2
		elif item == "cube":
			attr = "_cube_base"
			return object.__getattribute__(self, attr) ** 3
		else:
			return object.__getattribute__(self, item)

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
