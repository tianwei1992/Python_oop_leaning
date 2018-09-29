class CardHolder:
	acctlen = 8 # Class data
	retireage = 59.5

	def __init__(self, acct, name, age, addr):
		self.acct = acct # Instance data
		self.name = name # These trigger __setattr__ too
		self.age = age # acct not mangled: name tested
		self.addr = addr # addr is not managed

	def __getattribute__(self, name):
		superget = object.__getattribute__ # Don't loop: one level up
		if name == 'acct': # On all attr fetches
			return superget(self, 'acct')[:-3] + '***'
		elif name == 'remain':
			return superget(self, 'retireage') - superget(self, 'age')
		else:
			return superget(self, name) # name, age, addr: stored

	def __setattr__(self, name, value):
		if name == 'name': # On all attr assignments
			value = value.lower().replace(' ', '_') # addr stored directly
		elif name == 'age':
			if value < 0 or value > 150:
				raise ValueError('invalid age')
		elif name == 'acct':
			value = value.replace('-', '')
			if len(value) != self.acctlen:
				raise TypeError('invald acct number')
		elif name == 'remain':
			raise TypeError('cannot set remain')
		self.__dict__[name] = value # Avoid loops, orig names


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
1、这里，不管是否定义，每次属性获取都会捕获，因此，我们测试属性名称来检测管理的属性，并将所有其他的 属性指向超类以实现常规的获取过程。

2、这个版本和前面的版本一样，使用了同样的 __setattr__来捕获赋值。
注意，由于每个属性获取都指向了 __getattribute__，所以这里我们不需要压缩名称以 
拦截它们（ acct 存储为 _acct ）。另一方面，这段代码必须负责把未压缩的属性获取指向 
一个超类以避免循环。

3、对于设置和获取未管理的属性（例如， addr ），这个版本都会引发额外调 
用。如果速度极为重要，这个替代方法是4个方案中最慢的。
"""