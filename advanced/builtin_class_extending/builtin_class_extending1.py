# 1)通过委托，内置类型嵌入自定义类
class Set:
	"""用内置List实现的Set(其实也可以用内置dict实现）"""
	def __init__(self, value=[]):
		self.data = []
		self.concat(value)
	def intersect(self, other):
		"""取交集"""
		res = []
		for x in self.data:
			if x in other:
				res.append(x)
		return Set(res)
	def union(self, other):
		"""取并集"""
		res = self.data[:]
		for x in other:
			if x not in res:
				res.append(x)
		return Set(res)
	def concat(self, value):
		"""连接，把value中有自己没有的加上"""
		for x in value:
			if not x in self.data:
				self.data.append(x)

	def __len__(self):
		return len(self.data)
	def __getitem__(self, key):
		return self.data[key]
	def __and__(self, other):
		return self.intersect(other)
	def __or__(self, other):
		return self.union(other)
	def __repr__(self):
		return "Set: " + repr(self.data)


if __name__ == "__main__":
	x = Set([1, 3, 5, 7])
	print(x.union(Set([1, 4, 7])))
	print(x)