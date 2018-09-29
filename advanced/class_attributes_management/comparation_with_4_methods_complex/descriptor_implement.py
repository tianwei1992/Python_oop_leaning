class CardHolder:

	acctlen = 8 # Class data
	retireage = 59.5

	def __init__(self, acct, name, age, addr):
		self.acct = acct # Instance data
		self.name = name # These trigger __set__ calls too
		self.age = age # __X not needed: in descriptor
		self.addr = addr # addr is not managed

	class Name:

		def __get__(self, instance, owner): # Class names: CardHolder locals
			return self.name

		def __set__(self, instance, value):
			value = value.lower().replace(' ', '_')
			self.name = value

	name = Name()

	class Age:
		def __get__(self, instance, owner):
			return self.age # Use descriptor data

		def __set__(self, instance, value):
			if value < 0 or value > 150:
				raise ValueError('invalid age')
			else:
				self.age = value

	age = Age()

	class Acct:
		def __get__(self, instance, owner):
			return self.acct[:-3] + '***'

		def __set__(self, instance, value):
			value = value.replace('-', '')
			if len(value) != instance.acctlen: # Use instance class data
				raise TypeError('invald acct number')
			else:
				self.acct = value

	acct = Acct()

	class Remain:
		def __get__(self, instance, owner):
			return instance.retireage - instance.age  # Triggers Age.__get__
		def __set__(self, instance, value):
			raise TypeError('cannot set remain')  # Else set allowed here

	remain = Remain()


if __name__ == "__main__":
	bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
	print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
	bob.name = 'Bob Q. Smith'
	bob.age = 50
	bob.acct = '23-45-67-89'
	print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
	sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
	print(sue.acct, sue.name, sue.age, sue.remain, sue.addr, sep=' / ')
	try:
		sue.age = 200
	except:
		print('Bad age for Sue')
	try:
		sue.remain = 5
	except:
		print("Can't set sue.remain")
	try:
		sue.acct = '1234567'
	except:
		print('Bad acct for Sue')

"""
Notes:
1\要理解这段代码，注意 __init__ 构造函数方法内部的属性赋值触发了描述符的 __set__ 操 作符方法，这一点还是很重要。例如，当构造函数方法分配给 self.name 时，它自动调 
用 Name.__set__() 方法，该方法转换值，并且将其赋给了叫做 name 的一个描述符属性。 

2、和前面基于特性的变体不同，在这个例子中，实际的 name 值附加到了描述符对象，而不 
是客户类实例。尽管我们可以把这个值存储在实例状态或描述符状态中，后者避免了需 
要用下划线压缩名称以避免冲突。在 CardHolder 客户类中，名为 name 的属性总是一个描 
述符对象，而不是数据。

3、提供一个名为 remain 的只读属性， remain 是完全虚拟的并且根据需要计算。

4、注意我们为何在其描述符中捕获对 remain 的赋值，并引发一个异常。 
正如我们前面所介绍的，描述符不定以__set__并不能禁止赋值，对一个实例这一属性的赋值，将会默默地创 建一个实例属性而隐藏了类属性描述符。
"""