class Squares:
	def __init__(self, start, stop):
		self.value = start - 1
		self.stop = stop
	def __iter__(self):
		return self
	def __next__(self):
		if self.value == self.stop:
			print(self,self.value, "stop")
			raise StopIteration
		self.value += 1
		return self.value ** 2

if __name__ == "__main__":

	for i in Squares(1, 5):
		print(i, end=' ')
	print()
	X = iter(Squares(1, 5))    # X是迭代器
	print(next(X))
	print(next(X))
	print(next(X))