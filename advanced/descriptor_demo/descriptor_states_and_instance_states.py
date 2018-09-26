"""描述符状态和实例状态

描述符可以从不同的地方获取其信息:
1使用存储在客户实例中的数据，
2 第二个例子（属性乘方的例子）使用附加到描述符对象本身的数据。
实际上，描述符可以使用实例状态和描述符状态，或者二者的任何组合：

# 描述符状态用来管理内部用于描述符工作的数据。
# 实例状态记录了和客户类相关的信息，以及可能由客户类创建的信息。

描述符和实例状态都有各自的用途。实际上，这是描述符优于特性的一个通用优点——
因为它们都有自己的状态，所以可以很容易地在内部保存数据，而不用将数据添加到客
户实例对象的命名空间中。


"""

"""Example 1"""
# value是由描述符状态保存的
# 如果在客户类的实例中使用相同的名字
class DescState: # Use descriptor state
	def __init__(self, value):
		self.value = value
	def __get__(self, instance, owner): # On attr fetch
		print('DescState get')
		return self.value * 10
	def __set__(self, instance, value): # On attr assign
		print('DescState set')
		self.value = value

# Client class
class CalcAttrs:
	X = DescState(2) # Descriptor class attr
	Y = 3 # Class attr
	def __init__(self):
		self.Z = 4 # Instance attr

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z) # X is computed, others are not
obj.X = 5 # X assignment is intercepted
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)
print()

"""Example 2"""
# value是由客户实例保存的
class InstState: # Using instance state
	def __get__(self, instance, owner):
		print('InstState get') # Assume set by client class
		return instance._Y * 100
	def __set__(self, instance, value):
		print('InstState set')
		instance._Y = value

# Client class
class CalcAttrs:
	X = DescState(2)
	Y = InstState()  # Descriptor class attr

	def __init__(self):
		self._Y = 3  # Instance attr
		self.Z = 4  # Instance attr

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)  # X and Y are computed, Z is not
obj.X = 5  # X and Y assignments intercepted
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)