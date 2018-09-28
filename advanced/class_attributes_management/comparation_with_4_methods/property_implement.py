class Powers():
	def __init__(self, square_base, cube_base):
		self.square_base = square_base
		self.cube_base = cube_base
	def fget_square(self):
		return self.square_base ** 2

	def fget_cube(self):
		return self.cube_base ** 3

	def fset_square(self, value):
		self.square_base = value

	def fset_cube(self, value):
		self.cube_base = value

	square = property(fget_square, fset_square)
	cube = property(fget_cube, fset_cube)


X = Powers(3, 4)
print(X.square) # 3 ** 2 = 9
print(X.cube) # 4 ** 3 = 64
X.square = 5
print(X.square) # 5 ** 2 = 25


"""评注：
1、square = property(fget_square, fset_square)以及fget、fset两个方法的定义都是嵌套在在类的定义里面，而不是在类的定义之后追加。
2、书上示例中，self.square_base = square_base写作了self._square_base = square_base，默认想让外面看到的是square属性，self._square_base是辅助计算的一个值，倾向于被隐藏起来"""