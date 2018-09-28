class Powers():
	def __init__(self, square_base, cube_base):
		self._square_base = square_base
		self._cube_base = cube_base

	class SquareDescriptor():
		def __get__(self, instance, owner):
			if instance is None:
				"""类.attr - > Descriptor,没毛病"""
				return self
			return instance._square_base ** 2
		def __set__(self, instance, value):
			instance._square_base = value

	class CubeDescriptor():
		def __get__(self, instance, owner):
			if instance is None:
				return self
			return instance._cube_base ** 3
	square = SquareDescriptor()
	cube = CubeDescriptor()


X = Powers(3, 4)
"""Powers.square = 5不会触发SquareDescriptor.__get__方法，而是直接更改Powers.square为一个普通的属性，值为5，这也会影响到所以示例
所以结论:对标识符产生的属性，不要试图从类上面赋值。"""
print(Powers.square)
print()
print(X.square) # 3 ** 2 = 9
print(X.cube) # 4 ** 3 = 64
X.square = 5
print(X.square) # 5 ** 2 = 25


"""描述符定义的属性在类中定义，是类属性，但是get和set一般对实例用。

直接对类用set相当于覆盖原有属性为普通属性，偶尔对类用get，是类似Powers.square.__doc__的时候"""