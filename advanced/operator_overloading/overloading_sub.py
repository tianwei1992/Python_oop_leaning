class Number:
	def __init__(self, start):
		self.data = start
	def __sub__(self, other):
		return Number(self.data - other)

x = Number(5)
y = x - 2
z = 7 - x  # 重载只对左边的对象有效，这里报错TypeError: unsupported operand type(s) for -: 'int' and 'Number'
print(y.data)
print(z.data)