"""使用getattributes和getattributesibutes时注意避免循环"""

class Person:
	def __init__(self, name): # On [Person()]
		self._name = name # 2 Triggers __setattr__!
	def __getattribute__(self, attr): # On [obj.undefined]
		if attr == 'name':
			print('fetch...')
			attr = "_name"
			return object.__getattribute__(self, attr)  # 不能再用self._name，会发生递归
		else:  # Others are errors
			raise AttributeError(attr)
	def __setattr__(self, attr, value):  # On [obj.any = value]
		if attr == 'name':    # 3
			print('change...')
			attr = '_name'  # Set internal name
		object.__setattr__(self, attr, value) # 4 Avoid looping here
		# self.attr = value和self.__dict__[attr] = value都不能这样写，这样会转去调用setattr，发生循环
	def __delattr__(self, attr):  # On [del obj.any]
		if attr == 'name':
			print('remove...')
			attr = '_name'
		object.__delattr__(self, attr) # Avoid looping here too


bob = Person('Bob Smith')  # 1 bob has a managed attribute
print(bob.name)  # Runs __getattributes__
print(hasattr(bob, "_name"))
# print(bob._name)    这一句失效了，因为getattributes不会放过这个变量，尽管已经定义过了
bob.name = 'Robert Smith'  # Runs __setattr__
print(bob.name)
del bob.name  # Runs __delattr__
print('-' * 20)
sue = Person('Sue Jones')  # sue inherits property too
print(sue.name)

