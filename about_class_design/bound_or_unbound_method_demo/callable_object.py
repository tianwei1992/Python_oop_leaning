"""Python非常灵活，可调用对象有各种类型。
除了绑定方法，函数、类的方法、实例对象、类对象，都是可调用对象。"""
def square(arg):
	return arg ** 2

class Sum:
	def __init__(self, val):
		self.val = val
	def __call__(self, arg):
		"""sobject（5）调用实例时会执行这里"""
		return self.val + arg

class Product:
	def __init__(self, val):
		self.val = val
	def method(self, arg):
		return self.val * arg

class Negate:
	def __init__(self, val):
		self.val = -val
	def __repr__(self):
		return str(self.val)

sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method, Negate]
# 不管是函数、类的方法、实例对象、类对象，都是可调用的。在下面的循环中，就是依次调用这些可调用对象，给的参数是5。

for act in actions:
	"""这4个是完全等效的"""
	print(act(5))