"""Class interfaces"""

class Super:
	"""as a Abstract superclass, can't be instantialed until self.action func is realized"""
	def method(self):
		print("in Super.method")
	def delegate(self):
		self.action()

class Inheritor(Super):
	pass

class Replacer(Super):
	def method(self):
		print('in Replace.method')

class Extender(Super):
	"""覆盖并回调默认method，从而定制Super的method"""
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