# 2)继承内置类型，然后部分地通过重载改变内置类型的行为
class MyList(list):
	"""下标从0开始的list"""
	def __getitem__(self, offset):
		print("indexing {} at {}".format(self, offset))
		return list.__getitem__(self, offset - 1)

if __name__ == "__main__":
	x = MyList("abc")
	print(x[1])
	print()
	# 改变了下标，同时也继承了内置List方法
	print(x)
	print(list('abc'))
	x.append("5")
	x.reverse()
	print(x)