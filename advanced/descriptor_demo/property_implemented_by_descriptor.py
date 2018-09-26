"""用描述符实现特性，既然特性是描述符的特例
为了达到近似等效，考虑描述符定义属性和property定义属性的形式：

attr1 = DescriptorClass([init_args])
attr2 = property(fget, fset, fdel, fdoc)
实际上，客户类的实例调用属性时，会被拦截，转去执行描述符的比如_get__方法、如果是特性property，效果应该是执行定义时传入的fget函数。
因此，这里要做的就是把两件事映射起来，也就是在Descriptor实例的_get__的方法中调用fget函数，并传参。为此在Descriptor初始化的时候要找个位置保存一下fget。"""

class Property:
	def __init__(self, fget=None, fset=None, fdel=None, doc=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel # Save unbound methods
		self.__doc__ = doc # or other callables
	def __get__(self, instance, instancetype=None):
		if instance is None:
			return self
		if self.fget is None:
			raise AttributeError("can't get attribute")
		return self.fget(instance) # Pass instance to self in property accessors
	def __set__(self, instance, value):
		if self.fset is None:
			raise AttributeError("can't set attribute")
		self.fset(instance, value)

	def __delete__(self, instance):
		if self.fdel is None:
			raise AttributeError("can't delete attribute")
		self.fdel(instance)



"""
getName和setName为什么不写在Person内？
getName和setName是对属性Name的操作，是为了定义属性Name而写的，所以在把Name添加成Person的一个attr之前，这两个函数跟Person不应该有任何关系

其实这两个函数跟property还是class Property都没有绑定关系，无论用哪一个，都是被调用而已。今天调用的是你，明天可能调用是它。这里来无数个getName2、getName3……随便调用其中一个都可以
property是去调用fget函数，Property是首先调用自身的__get__方法，__get__转而去调用fget函数，所以是等效的，但这个等效与fget函数究竟是getName还是getName2、getName3没有关系"""
def getName(self):
	print("getName:{}".format(self._name))
def setName(self, value):
	print(self)
	self._name = value
	print("setName:{}".format(self._name))

#自定义的Property实现了与property同样的效果。
class Person:
	"""client class"""
	def __init__(self, name):
		self._name = name
	name = Property(getName, setName)  # Use like property()

grace = Person("grace")
print(grace.name)
grace.name = "grace2"
print(grace.name)

