class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances += 1
	def printNumInstances(cls):
		print("Number of instances:", cls.numInstances)
	printNumInstances = classmethod(printNumInstances)


if __name__ == "__main__":
	a,b = Spam(), Spam()
	a.printNumInstances()
	Spam.printNumInstances()
	print()


class Sub(Spam):
	def printNumInstances(cls):
		print("Extra stuff...", cls)
		Spam.printNumInstances()
	printNumInstances = classmethod(printNumInstances)


if __name__ == "__main__":
	x, y = Sub(), Spam()
	x.printNumInstances()
	y.printNumInstances()
	Sub.printNumInstances()
	print()


class Other(Spam):
	pass

if __name__ == "__main__":
	z = Other()
	z.printNumInstances()




