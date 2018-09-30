"""Examole 1 结果为数值"""
class Commuter:
	def __init__(self, val):
		self.val = val
	def __add__(self, other):
		print("add", self.val, other)
		return self.val + other
	def __radd__(self, other):
		print("radd", self.val, other)
		return other + self.val


if __name__ == "__main__":
	x = Commuter(88)
	y = Commuter(99)
	print(x + 1)
	print()
	print(1 + y)
	print()
	print(x + y)
	print("=" * 20)

"""Examole 2 结果为新对象"""
class Commuter:
	def __init__(self, val):
		self.val = val
	def __add__(self, other):
		if isinstance(other, Commuter):
			other = other.val
		return Commuter(self.val + other)
	def __radd__(self, other):
		return Commuter(self.val + other)
	def __iadd__(self, other):
		"""不定义的话，+=重载成__add__，也是没有问题的。只不过这个效率更高"""
		self.val += other
		return self
	def __str__(self):
		return "<Commuter: {}>".format(self.val)

if __name__ == "__main__":
	x = Commuter(88)
	y = Commuter(99)
	print(x + 10)
	print(10 + y)
	z = x + y
	print(z)
	print(z + 10)
	print(z + z)
	print()
	z += 1
	print(z)