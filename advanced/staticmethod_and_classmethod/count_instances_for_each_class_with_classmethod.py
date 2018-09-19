class Spam:
	numInstances = 0
	def count(cls):
		"""之前子类也是调用父类的init，子类没有自己的numInstances，所以计数一直在父类上"""
		cls.numInstances += 1
	def __init__(self):
		"""会传入self参数，表示把当前实例传进count，从而实现对当前类计数"""
		self.count()
	count = classmethod(count)

class Sub(Spam):
	"""有了自己的计数变量"""
	numInstances = 0
	def __init__(self):
		"""虽然调用的是父类init方法，但是最终会操作到自己的计数变量"""
		Spam.__init__(self)

class Other(Spam):
	numInstances = 0


if __name__ == "__main__":
	x = Spam()
	y1, y2 = Sub(), Sub()
	z1, z2, z3 = Other(), Other(), Other()

	print(x.numInstances, y1.numInstances, z1.numInstances)
	print(Spam.numInstances, Sub.numInstances, Other.numInstances)