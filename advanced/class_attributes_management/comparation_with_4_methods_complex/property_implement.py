class CardHolder:
    acctlen = 8 # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct # Instance data
        self.name = name # These trigger prop setters too
        self.age = age # __X mangled to have class name
        self.addr = addr # addr is not managed

    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(getName, setName)
    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value
            age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'

    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invald acct number')
        else:
            self.__acct = value

    acct = property(getAcct, setAcct)
    def remainGet(self): # Could be a method, not attr
        return self.retireage - self.age # Unless already using as attr

    remain = property(remainGet)


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
[注意命名]
由于property在类定义时的作用，self.name是特性定义的属性，self._name才是真正存储数据的属性，两者是不同的。
要理解这段代码，关键是要注意到，__init__构造函数方法内部的属性赋值也触发了特 
性的 setter 方法。例如，当这个方法分配给 self.name 时，它自动调用 setName 方法，该 
方法转换值并将其赋给一个叫做 __name 的实例属性，以便它不会与特性的名称冲突。 
这一重命名（有时候叫做名称压缩）是必要的，因为特性使用公用的实例状态并且没有 
自己的实例状态。存储在一个属性中的数据叫做 __name ，而叫做 name 的属性总是特性， 
而非数据。

---------------------

本文来自 minghu9 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/minghu9/article/details/53858404?utm_source=copy 
"""