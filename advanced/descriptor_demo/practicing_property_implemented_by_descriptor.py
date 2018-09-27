"""用描述符实现property比较复杂，再写一遍"""

class Property:
	def __init__(self, fget=None, fset=None, fdel=None, fdoc=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
		self.__doc__ = fdoc
	def __get__(self, instance, owner):
		if instance is None:
			return self    # 为了Person.name.__doc__可以正常显示！
		if self.fget is None:
			raise AttributeError("self.fget is None")
		return self.fget(instance)
	def __set__(self, instance, value):
		if self.fset is None:
			raise AttributeError("self.fget is None")
		self.fset(instance, value)
	def __delete__(self, instance):
		if self.fdel is None:
			raise AttributeError("self.fget is None")
		del instance._name

def fget(instance):
	print("in fget")
	return instance._name #如果写instance.name会引起无尽的递归,grace.name -> Property._get_-> fget(grace) -> grace.name
def fset(instance, value):
	print("in fset")
	instance._name = value
def fdel(instance):
	print("in fdel")
	del instance._name
	del self

def fdoc():
	return "grace docs in fdoc "

class Person:
	def __init__(self, name):
		self._name = name
	name = Property(fget, fset, fdel, fdoc())

if __name__ == "__main__":
	grace = Person("grace")
	print(grace.name)
	grace.name = "grace2"

	print(grace.name)
	print(Person.name.__doc__)
	del grace.name
	print(grace.name)