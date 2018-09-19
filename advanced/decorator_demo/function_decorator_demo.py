"""函数装饰器"""
class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args, **kwargs):
		self.calls += 1
		print("call {} to {}".format(self.calls, self.func.__name__))
		self.func(*args)


@tracer
def spam(a, b, c):
	print(a, b, c)

spam(1, 2, 3)
spam('a', 'b', 'c')
spam(4, 5, 6)