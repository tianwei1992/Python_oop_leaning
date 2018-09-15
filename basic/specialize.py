"""Class interfaces & Abstract superclass"
About:
    How to extends a Super class?
    How to specialize a abstract superclass?""

class Super:
	"""as a Abstract superclass, can't be instantialed until self.action func is realized"""
	def method(self):
		print("in Super.method")
	def delegate(self):
		self.action()
	def action(self):
		raise NotImplementedError("action must be defined")

class Inheritor(Super):
	"""原样继承"""
	pass

class Replacer(Super):
	"""通过完全替换覆盖原方法，实现定制"""
	def method(self):
		print('in Replace.method')

class Extender(Super):
	"""通过回调默认method和扩展覆盖原方法，实现定制"""
	def method(self):
		print("starting Extender.method")
		Super.method(self)
		print("ending Extender.method")

class Provider(Super):
	"""实现了抽象超类Super的action方法，于是Super才可以被实例化"""
	def action(self):
		print("in Provider.action")


if __name__ == "__main__":
	for klass in (Inheritor, Replacer, Extender):
		print("\n" + klass.__name__ + "...")
		klass().method()

	print("\nProvider...")
	x = Provider()
	x.delegate()
	y = Replacer()
	y.delegate()