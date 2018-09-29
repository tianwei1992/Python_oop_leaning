class Person:
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))
	def __str__(self):
		return '[Person: %s, %s]' % (self.name, self.pay)

class Manager:
	def __init__(self, name, pay):
		self.person = Person(name, 'mgr', pay)  # Embed a Person object
	def giveRaise(self, percent, bonus=.10):
		self.person.giveRaise(percent + bonus)  # Intercept and delegate
	def __getattr__(self, attr):
		return getattr(self.person, attr)  # Delegate all other attrs
	# def __str__(self):
	# 	return str(self.person)  # Must overload again (in 3.0)


if __name__ == '__main__':
	sue = Person('Sue Jones', job='dev', pay=100000)
	print(sue.lastName())
	sue.giveRaise(.10)
	print(sue)
	tom = Manager('Tom Jones', 50000)  # Manager.__init__
	print(tom.lastName())  # Manager.__getattr__ -> Person.lastName
	tom.giveRaise(.10)  # Manager.giveRaise -> Person.giveRaise
	print(tom)  # Manager.__str__ -> Person.__str__

"""
删除了Manager.__str__方法，调用print(tom)时本来希望借助触发Manager.__getattr__方法，去调用Person.__str__，但实际上并不是这样。调用print(tom)并没有Manager.__getattr__

"""