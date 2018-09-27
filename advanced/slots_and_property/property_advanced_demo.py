class Person:
	"""name = property(name)，property返回的是一个property对象，可以继续有property.setter、deleter继续装饰"""
	def __init__(self, name):
		self._name = name
	@property
	def name(self): # name = property(name)
		"name property docs"
		print('fetch...')
		return self._name
	@name.setter
	def name(self, value): # name = name.setter(name)
		print('change...')
		self._name = value
	@name.deleter
	def name(self): # name = name.deleter(name)
		print('remove...')
		del self._name

bob = Person('Bob Smith') # bob has a managed attribute
print(bob.name) # Runs name getter (name 1)
bob.name = 'Robert Smith' # Runs name setter (name 2)
print(bob.name)
del bob.name # Runs name deleter (name 3)
print('-'*20)
sue = Person('Sue Jones') # sue inherits property too
print(sue.name)
print(Person.name.__doc__) # Or help(Person.name)

"""Notes：
现有普通的类属性self._name，然后为了方便管理，用property定义了特性name，但调用xx.name归根结底还是访问到self._name"""
