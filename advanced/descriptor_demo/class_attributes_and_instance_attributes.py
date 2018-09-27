class A(object):
	def __init__(self):
		self.a = 5


print(hasattr(A, "a")) # False
a = A()
print(hasattr(a, "a")) # False
print(a.a)  # 5
print(A.a)    # AttributeError: type object 'A' has no attribute 'a'