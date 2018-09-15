"""多重继承，ListInstance是其中一个父类，ListInstance的__str__依然有效"""
from lister import *

class Super:
	def __init__(self):
		self.data1 = "spam"
	def ham(self):
		pass

class Sub(Super, ListInstance):
	def __init__(self):
		Super.__init__(self)
		self.data2 = "eggs"
		self.data3 = 42
	def spam(self):
		pass

class SubInherited(Super, ListInherited):
	def __init__(self):
		Super.__init__(self)
		self.data2 = "eggs"
		self.data3 = 42
	def spam(self):
		pass

class SubTree(Super, ListTree):
	def __init__(self):
		Super.__init__(self)
		self.data2 = "eggs"
		self.data3 = 42
	def spam(self):
		pass

if __name__ == "__main__":
	X = Sub()
	print(X)
	Y = SubInherited()
	print(Y)
	Z = SubTree()
	print(Z)

	"""mix SubTree with a built-in class, i.e.,tkinter.Button,"""

	from tkinter import Button
	class MyButton(ListTree, Button):
		pass

	B = MyButton(text = "spam")
	print(B)