def factory(aClass, *args, **kwargs):
	"""工厂函数：把类传给能够产生任意种类对象的函数
	建立工厂时，需要传进来的类对象或者参数还不存在或者说他们的行为不确定……工厂就是这样一个函数，建立了工厂，只要类对象已确定，就可以马上通过工厂构造出对象"""
	return aClass(*args, **kwargs)

class Spam:
	def doit(self, message):
		print(message)

class Person:
	def __init__(self, name, job):
		self.name = name
		self.job = job


if __name__ == "__main__":
	object1 = factory(Spam)
	object2 = factory(Person, "Guido", "guru")

	object1.doit("hello")
