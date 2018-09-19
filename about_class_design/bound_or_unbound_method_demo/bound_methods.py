class Number:
	def __init__(self, base):
		self.base = base
	def double(self):
		return self.base * 2
	def triple(self):
		return self.base * 3

x = Number(2)
y = Number(3)
z = Number(4)

acts = [x.double, y.double, y.triple, z.double]
for act in acts:
	print(act())

bound = x.double
"""绑定方法拥有自己的内省信息，包括自己是一个什么对象，以及绑定的func"""
print(bound.__self__)    # <__main__.Number object at 0x01706970>这是一个对象和class Number不等价的
print(Number)    # <class '__main__.Number'>
# print(bound.__self__.__bases__)   # 这回报错
print(bound.__func__)    # <function Number.double at 0x014090C0>

def squre
