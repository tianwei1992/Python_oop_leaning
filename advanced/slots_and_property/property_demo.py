"""老的例子"""
class classic:
	def __getattr__(self, name):
		if name == 'age':
			return 40
		else:
			raise AttributeError
	def __setattr__(self, name, value):
		print("set {},{}".foramt(name, value))
		if name == "age":
			self.__dict__["_age"] = value
		else:
			self.__dict__[name] = value

x = classic()
print(x.age)
# print(x.name)

class newprops(object):
	def getage(self):
		return 40
	def setage(self, value):
		print("set age: {}".format(value))
		self._age = value
	"""注意这些函数的命名"""
	age = property(getage, setage, None, None)

x = newprops()
print(x.age)
x.age = 50
print(x._age)
x.name = "bob"
print(x.name)