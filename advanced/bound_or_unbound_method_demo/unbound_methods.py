"""
9、类方法有2种调用，通过实例调用和通过类调用，其中通过类调用必须手动传递实例。通过实例调用是自动转换成第二种。
第一种返回 ubound类方法对象，调用这个方法时，需要提供一个实例对象做参数（Python3不需要了已经，只要这个方法本身第一个参数不需是self）
第二种返回bound实例方法对象，不用传递实例。

这也是[为什么类方法为什么 要有第一个参数self？]
instance.method(args) -> class.method(instance,args)
类可以产生很多实例，用类名.方法名时需要这样来区分是哪个实例。

"""
class Selfless:
	def __init__(self, data):
		self.data = data
	def selfless(arg1, arg2):
		"""注意这个方法不需要传入第一个self参数"""
		return arg1 + arg2
	def normal(self, arg1, arg2):
		return self.data + arg1 + arg2

X = Selfless(2)
print(X.normal(3, 4))    # 9

print(Selfless.normal(X, 3, 4))      # 9
print(Selfless.selfless(3, 4))    # 7 在Python2这就是一个unbound方法，这样用是错的，但是Python3可以，认为这就是一个普通函数
