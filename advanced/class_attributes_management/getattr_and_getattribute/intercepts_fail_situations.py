"""试探getattr和getattributes对内置的__str__\__call__等是否有效，在没有专门重载的时候情况下"""

class GetAttr:
	eggs = 88 # eggs stored on class, spam on instance
	def __init__(self):
		self.spam = 77
	def __len__(self): # len here, else __getattr__ called with __len__
		print('__len__: 42')
		return 42
	def __getattr__(self, attr): # Provide __str__ if asked, else dummy func
		print('getattr: ' + attr)
		if attr == '__str__':
			return lambda *args: '[Getattr str]'
		else:
			return lambda *args: None

class GetAttribute(object): # object required in 2.6, implied in 3.0
	eggs = 88 # In 2.6 all are isinstance(object) auto
	def __init__(self): # But must derive to get new-style tools,
		self.spam = 77 # incl __getattribute__, some __X__ defaults
	def __len__(self):
		print('__len__: 42')
		return 42
	def __getattribute__(self, attr):
		print('getattribute: ' + attr)
		if attr == '__str__':
			return lambda *args: '[GetAttribute str]'
		else:
			return lambda *args: None


for Class in GetAttr, GetAttribute:
	print('\n' + Class.__name__.ljust(50, '='))
	X = Class()
	X.eggs # Class attr
	X.spam # Instance attr
	X.other # Missing attr
	len(X) # __len__ defined explicitly
	try: # New-styles must support [], +, call directly: redefine
		X[0] # __getitem__?
	except:
		print('fail []')
	try:
		X + 99 # __add__?
	except:
		print('fail +')
	try:
		X() # __call__? (implicit via built-in)
	except:
		print('fail ()')
	X.__call__() # __call__? (explicit, not inherited)
	print(X.__str__()) # __str__? (explicit, inherited from type)
	print(X) # __str__? (implicit via built-in)


"""
Conclusion:
在Python 2.6下运行的时候，__g e t a t t r__的确接收针对内置操作的各种隐式属性获
取，因为P y t h o n通常在实例中查询这样的属性。相反，对于任何操作符重载名，
__getattribute__不会运行，因为这样的名称只在类中查找：
注意，在Python 2.6中，这里的__getattr__如何拦截__call__和__str__的隐式和显式获
取。相反，对于内置操作的任何属性名，__getattribute__不能捕捉隐式获取
"""