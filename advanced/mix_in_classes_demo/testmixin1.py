from lister import ListInstance
"""直接继承ListInstance，ListInstance的__str__有效"""
class Spam(ListInstance):
	def __init__(self):
		self.data1 = "food"

x = Spam()
print(x)