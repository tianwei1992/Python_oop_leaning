"""Assorted Class Utilities and tools
各种类实用程序和工具"""

class AttrDisplay:
	"""为class提供print方法的重载，打印内容包含class name以及键值对形式的instance.__dict"""
	def gatherAttrs(self):
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append("{}={}".format(key, getattr(self, key)))
		return ','.join(attrs)

	def __str__(self):
		return "[{} {}]".format(self.__class__.__name__, self.gatherAttrs())


if __name__ == "__main__":
	class TopTest(AttrDisplay):
		count = 0    # This attr specially defined for testing as attr not in instance.__dict__, it shouldn't be print out
		def __init__(self):
			self.attr1 = TopTest.count
			self.attr2 = TopTest.count + 1
			TopTest.count += 2

	class SubTest(TopTest):
		pass

	X, Y = TopTest(), SubTest()
	print(X)
	print(Y)

