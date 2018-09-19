class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances += 1
	def printNumInstances():
		print("Num of instances:", Spam.numInstances)
	printNumInstances = staticmethod(printNumInstances)


if __name__ == "__main__":
	a = Spam()
	b = Spam()
	c = Spam()
	a.printNumInstances()
	Spam.printNumInstances()
	print()


class Sub(Spam):
	"""子类没有自己的计数器，也没有重载init方法以为着每次init时会执行父类的Spam.numInstances += 1"""
	def printNumInstances():
		print("Extra stuff...")
		Spam.printNumInstances()
	printNumInstances = staticmethod(printNumInstances)

if __name__ == "__main__":
	a = Sub()
	b = Sub()
	a.printNumInstances()
	"""会去调用父类Spam.printNumInstances()，通过类名调用.
	因为init没有重载，每次Sub实例化就会执行Spam.numInstances += 1"""
	a.printNumInstances()
	Sub.printNumInstances()
	print()

class Other(Spam):
	pass

if __name__ == "__main__":
	c = Other()
	c.printNumInstances()