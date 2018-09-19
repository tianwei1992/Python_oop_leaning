""""""
class C:
	__slots__ = ['a', 'b']
	"""disallowed:AttributeError: 'C' object has no attribute 'd,undelss __dict__ is added to __slot__'
	def __init__(self):
		self.d = 4
	"""


x = C()
x.a = 1
print(x.a)

"""AttributeError: 'C' object has no attribute '__dict__'
print(x.__dict__)
"""
print(getattr(x, "a"))
setattr(x, 'b', 2)
print(dir(x))


class D:
	__slots__ = ['a', 'b', '__dict__']
	c = 3
	def __init__(self):
		self.d = 4

d = D()
print(d.d)
print(d.__dict__)    # {'d': 4}
print(d.__slots__)   # ['a', 'b', '__dict__']

d.a = 1
d.b = 2
"""查看完整属性"""
for attr in list(d.__dict__) + x.__slots__:
	print("{} => {}".format(attr, getattr(d, attr)))

