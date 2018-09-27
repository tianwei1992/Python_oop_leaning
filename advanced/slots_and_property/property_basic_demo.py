"""老的例子"""
class classic:
	def __getattr__(self, name):
		if name == 'age':
			return 40
		else:
			raise AttributeError
	def __setattr__(self, name, value):
		print("set {},{}".foramt(name, value))
		if name == "age":
			self.__dict__["_age"] = value
		else:
			self.__dict__[name] = value

x = classic()
print(x.age)
# print(x.name)

"""用property简化"""
class newprops(object):
	def getage(self):
		return 40
	def setage(self, value):
		print("set age: {}".format(value))
		self._age = value
	"""注意这些函数的命名"""
	age = property(getage, setage, None, None)

x = newprops()
print(x.age)
x.age = 50
print(x._age)
x.name = "bob"
print(x.name)


class PropSquare:
	"""通过property关键字，X成为了一个属性。
	不过特殊之处在于，看起来是在取得一个静态的值，但每次执行获取属性这个操作的时候，还调用了方法，值都在变化
	这种效果很像是一个隐式方法调用。当代码运行的时候，
值作为状态信息存储在实例中，但是，每次我们通过管理的属性获取它的时候，它的值
都会自动平方：
	"""
	def __init__(self, start):
		self.value = start
	def getX(self): # On attr fetch
		return self.value ** 2
	def setX(self, value): # On attr assign
		self.value = value
	X = property(getX, setX) # No delete or docs
P = PropSquare(3) # 2 instances of class with property
Q = PropSquare(32) # Each has different state information
print(P.X) # 3 ** 2
P.X = 4
print(P.X) # 4 ** 2
print(Q.X) # 32 ** 2

"""
Notes:
这里涉及到了2个属性：
客户类本来的属性self.value和property定义的X, 也就是第一个例子中的self.age和self._age.
前者就是最简单的类的属性，后者是为了方便对前者的管理而诞生的。
实际数据保存在前者。
通过对后者的访问，本质上去访问到前者

"""