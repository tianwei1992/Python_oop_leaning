class Powers():
	def __init__(self, square_base, cube_base):

		self.__dict__["square_base"] = square_base
		self.__dict__["cube_base"] = cube_base
	def __getattribute__(self, item):
		if item == "square":
			attr = "square_base"
			return object.__getattribute__(self, attr) ** 2
		elif item == "cube":
			attr = "cube_base"
			return object.__getattribute__(self, attr) ** 3
		else:
			return object.__getattribute__(self, item)

	def __setattr__(self, key, value):
		if key == "square":
			self.__dict__["square_base"] = value
		elif key == "cube":
			self.__dict__["cube_base"] = value
		else:
			raise AttributeError()

X = Powers(3, 4)
print(X.square) # 3 ** 2 = 9
print(X.cube) # 4 ** 3 = 64
X.square = 5
print(X.square) # 5 ** 2 = 25


"""
开始的考虑：
初始化时__dict__不会触发getattr但是会触发getattribute，所以getattribute里面不能再写__dict__，否则就是无限递归……
用object.__getattribute__(self, attr) ** 2

问题：
1、init赋值时用的self.__dict__["square_base"] = square_base这种形式而不是直接xx.yy，当时的考虑是为了避免触发setattr。当时的setattr自身有问题，对除开squre和cube两者以外的其他属性赋值均做报错——这当然是不符合逻辑的。
只要改正setattr的这个问题，init就可以用更简单的形式。
2、过程变量名记得加个下划线隐藏起来，self._square_base这样。
3、在_getattribute__里面用return object.__getattribute_(self, attr) ** 2，这样是对了的，千万不能用dict。
"""