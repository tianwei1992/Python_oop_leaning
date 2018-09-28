class Powers():
	def __init__(self, square_base, cube_base):
		self.square_base = square_base
		self.cube_base = cube_base

	class Descriptor():
		def __init__(self, attr):
			self.attr = attr

		def __get__(self, instance, owner):
			if instance is None:
				raise AttributeError()
			if self.attr == "square":
				return instance.square_base ** 2
			elif self.attr == "cube":
				return instance.cube_base ** 3

		def __set__(self, instance, value):
			if instance is None:
				raise AttributeError()
			if self.attr == "square":
				instance.square_base = value
			elif self.attr == "cube":
				instance.cube_base = value

	square = Descriptor("square")
	cube = Descriptor("cube")


X = Powers(3, 4)
print(X.square) # 3 ** 2 = 9
print(X.cube) # 4 ** 3 = 64
X.square = 5
print(X.square) # 5 ** 2 = 25


"""
开始的考虑：
描述符定义的属性不能通过类调用，只能通过实例调用？
问题：
这个版本是用一个描述符Descriptor()实现了2个不同的属性，区分就是依据__init__时传入的参数。
虽然运行是正确的，但是书上的思路更合理：每1个属性用1个描述符类实现。
首先是逻辑上合理，其次是代码更清晰，不像我的第一个版本需要各种if-else判断，如果属性再多几个肯定吃不消的……
"""

"""
回答开始的考虑：
描述符定义的属性在类中定义，是类属性，但是get和set一般对实例用。

直接对类用set相当于覆盖原有属性为普通属性，偶尔对类用get，是类似Powers.square.__doc__的时候"""