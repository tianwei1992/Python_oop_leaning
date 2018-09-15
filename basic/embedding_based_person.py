"""
类的嵌套：
    把Person类嵌入Manager类中，注意一些问题
注意：
    这不是一个好的例子，只是为了举例
    好例子是把Person和Manger一起嵌入Department中,见combining.py

"""

class Person:
	count = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return "Person: {} {}".format(self.name, self.age)


class Manager():
	def __init__(self, name, age, level):
		self.person = Person(name, age)
		self.person.level = level
		self.person.count += 1
	def __str__(self):
		"""__getattr__能够找到普通的属性，但是找不到隐式的属性，所以要自己定义"""
		return str(self.person)
	def __getattr__(self, attr):
		return getattr(self.person, attr)

if __name__ == "__main__":
	a = Person('a', 24)
	b = Manager('b', 25, "1")
	print(a.__dict__)
	print(a.__class__.__name__)
	print(b.__dict__)
	print(b.__class__.__name__)
	print(b.person.count)  # 首先能找到b有person特性，所以不会去调用__getattr__
	print(b.level)    # 首先不能找到b有level特性，所以调用__getattr__再找