"""通过__setattr__拦截赋值操作，屏蔽不应该的赋值"""
class PrivateExc(Exception):
	pass

class Privacy:
	def __setattr__(self, key, value):
		if key in self.privates:
			raise PrivateExc(key, self)

class Test1(Privacy):
	privates = ["age"]

class Test2(Privacy):
	privates = ["name", "pay"]
	def __init__(self):
		self.__dict__["name"] = "Tom"


if __name__ == "__main__":
	x = Test1()
	y = Test2()

	x.name = "x"
	y.age = 40
	try:
		y.name = "y"
	except:
		print("fail y.name")
	try:
		x.age = 30
	except:
		print("fail x.age")