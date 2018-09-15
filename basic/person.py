"""Define class Person and class Manager with inheriting from AttrDisplay"""
from classtools import AttrDisplay
class Person(AttrDisplay):
	def __init__(self, name, job, pay):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay = int(self.pay * (percent + 1))
	# def __str__(self):
	# 	return "Person---name:{},pay:{}".format(self.name, self.pay)


class Manager(Person):
	def __init__(self, name, pay):
		Person.__init__(self, name, 'manager', pay)
	def giveRaise(self, percent, bonus=.10):
		Person.giveRaise(self, percent + bonus)


if __name__ == "__main__":
	a = Person('a', 'worker', 10)
	b = Manager('b', 20)
	print(a)
	print(b)
	b.giveRaise(0.1)
	print(b)

	print("\nOther testing……")
	"""比较instance.__dict__,dir(instance)"""
	print(a.__dict__.keys())
	print(dir(a))
	"""使用instance.__class__,class.__base__"""
	print(a.__class__.__name__)    # Person
	print(b.__class__.__name__)    # Manager
	print(a.__class__.__base__)    # <class 'object'>
	print(b.__class__.__base__)    # <class '__main__.Person'>