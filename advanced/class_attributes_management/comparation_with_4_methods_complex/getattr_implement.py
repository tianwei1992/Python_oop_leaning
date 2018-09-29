class CardHolder:

    acctlen = 8 # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct # Instance data
        self.name = name # These trigger __setattr__ too
        self.age = age # _acct not mangled: name tested
        self.addr = addr # addr is not managed


    def __getattr__(self, name):
        if name == 'acct': # On undefined attr fetches
            return self._acct[:-3] + '***' # name, age, addr are defined
        elif name == 'remain':
            return self.retireage - self.age # Doesn't trigger __getattr__
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'name': # On all attr assignments
            value = value.lower().replace(' ', '_') # addr stored directly
        elif name == 'age': # acct mangled to _acct
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')

        self.__dict__[name] = value # Avoid looping


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
1、在我们的例子中，当获取一个管理属性的时候，我们通过直接测试属性名来获知。其他的属性物理地存储在实例中，因而无法达到__getattr__。尽管 
这种方法比使用特性或描述符更为通用，但需要额外的工作来模拟专门关注属性的其他 
工具。

2、我们需要在运行时检查名称，并且必须编写一个__setattr__ 以拦截并验证属性赋 
值。
对于这个例子的特性和描述符版本，注意 __init__ 构造函数方法中的属性赋值触发了类 
的 __setattr__ 方法，这还是很关键的。例如，当这个方法分配给 self.name 时，它自动 
地调用 setattr 方法，该方法转换值，并将其分配给一个名为 name 的实例属性。通过 
在该实例上存储 name ，它确保了未来的访问不会触发__getattr__ 。相反， acct 存储为 
_acct ，因此随后对 acct 的访问会调用 __getattr__ 。

3、还要注意，当对未管理属性进行set赋值（例如， addr，是普通属性但没有对应的管理属性 ）的时候，这里的代码引发额外调用，然而进行get获取不会引发额外调用，因为getattr会跳过已定义。
对特性和描述符不会存在这种开销：只有当访问某一个管理属性的时候，特性和描述符才会引发额外调用。
"""