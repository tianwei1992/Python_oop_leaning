"""绝大多数情况下，getattr和getattibute应该用于通用的委托
但这里举一个例子，让他们像特性property和标识符一样，定义一个可以动态计算的属性"""
class AttrSquare:
	def __init__(self, start):
		self.value = start # Triggers __setattr__!
	def __getattr__(self, attr): # On undefined attr fetch
		if attr == 'X':
			return self.value ** 2 # value is not undefined
		else:
			raise AttributeError(attr)
	def __setattr__(self, attr, value): # On all attr assignments
		if attr == 'X':
			attr = 'value'
		self.__dict__[attr] = value


A = AttrSquare(3) # 2 instances of class with overloading
B = AttrSquare(32) # Each has different state information
print(A.X) # 3 ** 2
A.X = 4
print(A.X) # 4 ** 2
print(B.X) # 32 ** 2