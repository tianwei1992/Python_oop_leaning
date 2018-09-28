"""使用getattr和getattributes时注意避免循环"""

class Person:
	def __init__(self, name): # On [Person()]
		self._name = name # 2 Triggers __setattr__!
	def __getattr__(self, attr): # On [obj.undefined]
		if attr == 'name':
			print('fetch...')
			return self._name  # Does not loop: real attr
			"""这里是getattr，只拦截为定义的属性，像self._name这种已存在的不会调用getattr所以可以这么写"""
		else:  # Others are errors
			raise AttributeError(attr)
	def __setattr__(self, attr, value):  # On [obj.any = value]
		if attr == 'name':    # 3
			print('change...')
			attr = '_name'  # Set internal name
		self.__dict__[attr] = value  # 4 Avoid looping here
		# self.attr = value 不能这样写，这样会转去调用setattr，发生循环
	def __delattr__(self, attr):  # On [del obj.any]
		if attr == 'name':
			print('remove...')
			attr = '_name'  # Avoid looping here too
		del self.__dict__[attr]  # but much less common


bob = Person('Bob Smith')  # 1 bob has a managed attribute
print(bob.name)  # Runs __getattr__
print(hasattr(bob, "_name"))
print(bob._name)
bob.name = 'Robert Smith'  # Runs __setattr__
print(bob.name)
del bob.name  # Runs __delattr__
print('-' * 20)
sue = Person('Sue Jones')  # sue inherits property too
print(sue.name)

