"""绝大多数情况下，getattr和getattibute应该用于通用的委托
但这里举一个例子，让他们像特性property和标识符一样，定义一个可以动态计算的属性"""

class AttrSquare:
	def __init__(self, start):
		self.value = start # Triggers __setattr__!
	def __getattribute__(self, attr): # On all attr fetches
		"""
		实际上，每次我们获取属性X的时候，__g e t a t t r i b u t e__都运行了两次。这并没有在__g e t a t t r__版本中发生，因为v a l u e属性没有定义。如果你关心速度并且要避免这一点，修改__getattribute__以使用超类来获取value：
		def __getattribute__(self, attr):
			if attr == 'X':
				return object.__getattribute__(self, 'value') ** 2
		"""
		if attr == 'X':
			return self.value ** 2 # Triggers __getattribute__ again!这里为了实现 对X**2，所以单独给了X一个if分支，区别对待，这回触发下一次调用，不过最终还是归到return object.__getattribute__(self, attr)上
		else:
			return object.__getattribute__(self, attr)
	def __setattr__(self, attr, value): # On all attr assignments
		if attr == 'X':
			attr = 'value'
		object.__setattr__(self, attr, value)


A = AttrSquare(3) # 2 instances of class with overloading
B = AttrSquare(32) # Each has different state information
print(A.X) # 3 ** 2
A.X = 4
print(A.X) # 4 ** 2
print(B.X) # 32 ** 2

