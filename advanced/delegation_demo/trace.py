class wrapper:
	"""一个简单的实现委托的类"""
	def __init__(self, object):
		"""object就是被包装的对象"""
		self.wrapped = object
	def __getattr__(self, attrname):
		print("Trace:", attrname)
		return getattr(self.wrapped, attrname)


if __name__ == "__main__":
	x = wrapper([1, 2, 3])
	x.append(4)     # append()调用了__getattr__
	print(x.wrapped)

	print()
	y = wrapper({"a":1,"b":2})
	print(y.keys())    # keys()调用了__getattr__