class Powers():
	def __init__(self, square_base, cube_base):
		self.__dict__["square_base"] = square_base
		self.__dict__["cube_base"] = cube_base
	def __getattr__(self, item):
		if item == "square":
			return self.__dict__["square_base"] ** 2
		elif item == "cube":
			return self.__dict__["cube_base"] ** 3
		else:
			raise AttributeError

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


"""开始的考虑：
初始化时self.square_base = square_base会调用setattr
于是init时 用dict

问题：
这个版本在init赋值时用上了dict，而不是最普通的self.square_base，就是为了防止跳转到setattr。因为我的setattr处理不了这种情况，对于"square"和“cube”之外的其他任何key会报错。
这么做是不对的：
1、setattr会拦截所以定义未定义的属性，即使是未定义的属性，我们也要让它可以被加进来，而不是不给加给报错。
2、另外看到，书上的init赋值就是正常的点号，这当然会被setattr拦截，没关系，在setattr里面考虑这种情况，就可以了。
3、在看到书上__getattr__内部实现获取并没有用dict而是直接用self._square。这正好体现__getattr__和__getattribute__的区别，前者因为只捕获未定义属性，所以换句话说，对于已定义的属性，可以放心的用self._square这种形式，不用担心再掉入一次__getattr__。也是这个原因，__getattr__在排除了"square"和"cube"这2个其实未定义但人为有概念的key之后，其他属性都是未定义的，就该默认报错。
"""