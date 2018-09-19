"""类装饰器
用装饰器装饰count_instances_for_each_class_with_classmethod"的计数器定义，从而代码行数更少
count_instances_for_each_class_with_classmethod中3个类的定义都有重复的一句话，这就是装饰器要代劳的
"""
def count(aClass):
	aClass.numInstances = 0
	return aClass

@count
class Spam:
	def count(cls):
		cls.numInstances += 1
	def __init__(self):
		self.count()
	count = classmethod(count)

@count
class Sub(Spam):
	numInstances = 0
	def __init__(self):
		Spam.__init__(self)

@count
class Other(Spam):
	numInstances = 0


if __name__ == "__main__":
	x = Spam()
	y1, y2 = Sub(), Sub()
	z1, z2, z3 = Other(), Other(), Other()

	print(x.numInstances, y1.numInstances, z1.numInstances)
	print(Spam.numInstances, Sub.numInstances, Other.numInstances)
