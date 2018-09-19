class E:
	__slots__ = ['c', 'd']

class D(E):
	"""子类有__slots__"""
	__slots__ = ["a", "__dict__"]

x = D()
"""x只继承了D的class"""
x.a = 1
x.b = 2
x.c = 3
print(x.a, x.b, x.c)

print(D.__slots__, E.__slots__)
print(x.__slots__)
print(x.__dict__)

class F(E):
	"""子类没有__slots__"""
	pass

f = F()
print(f.__slots__)
print(f.__class__.__base__.__slots__)
f.a = 1
print(f.__dict__)


class G(E):
	"""子类有__slots__且同名"""
	__slots__ = ["c"]
	E.c = 1

g = G()
g.c = 2
print(g.c)
print(E.c)
