"""不做特殊处理，这个对象不支持同时两个活动迭代器，会公用一个状态"""
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.insert(0, parentdir)
"""Refer: https://www.aliyun.com/jiaocheng/461993.html"""
from custom_iterator import Squares
X = Squares(1, 5)
print(X)
for x in X:
	for y in X:
		print("x = {}, y = {}".format(x, y))
		print(x + y)
print()

"""除非两个循环里用的是Square()的两个对象，也不行
原因是：当Y到达6，也就是第一次迭代到尽头之后，就不可能有下一轮迭代

首先X=1，Y一路从3、4、5、6.，正常
然后X = 2，开始第2轮……但此时Y作为迭代器已经迭代到尽头不可能重新再从3开始"""
X = Squares(1, 5)
Y = Squares(3, 6)
print(X)
print(Y)
for x in X:
	for y in Y:
		print("x = {}, y = {}".format(x, y))
		print(x + y)
print()

"""那是否就是不可能实现呢？我们看到内置的str类型明明可以实现这个效果"""
s = "qwe"
for i in s:
	for j in s:
		print(i + j)
print()

"""那么自定义的迭代器如何做到？"""

class SquaresCore:
	def __init__(self, start, stop):
		print("init...",self)
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

class Squares:
	def __init__(self, start, stop):
		self.start = start
		self.stop = stop
	def __iter__(self):
		return SquaresCore(self.start, self.stop)

if __name__ == "__main__":
	SC = Squares(1, 4)
	for x in SC:
		for y in SC:
			print(x , y)
