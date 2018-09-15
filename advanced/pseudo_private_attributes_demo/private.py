"""demonstrate what will happen if pseudo_private attributes is not used when one inherit a attribute of the same name in different methods belong to different superclasses
"""
class C1:
	def meth1(self):
		self.X = 88
	def meth2(self):
		print(self.X)

class C2:
	def metha(self):
		self.X = 89
	def methb(self):
		print(self.X)

class SubC(C１, C2):
	pass
sc1 = SubC()
sc1.meth1()
sc1.metha()
sc1.meth2()    # 89
sc1.methb()    # 89

sc2 = SubC()
sc2.metha()
sc2.meth1()
sc2.meth2()    # 88
sc2.methb()    # 88


"""From the results we can see,When confilicts the results depends on the exec sequence of the relating methods, always the last one win.This is unexpected.
To fix this ,using pseudo private attributes starting with "__",Python will add class name prefix at the begining automaticlly, so there will be two different variables in fact with no confilicts.
^"""
print("\nFixing...\n")
class C1:
	def meth1(self):
		self.__X = 88
	def meth2(self):
		print(self.__X)

class C2:
	def metha(self):
		self.__X = 89
	def methb(self):
		print(self.__X)

class SubC(C１, C2):
	pass
sc1 = SubC()
sc1.meth1()
sc1.metha()
sc1.meth2()    # 88
sc1.methb()    # 89

sc2 = SubC()
sc2.metha()
sc2.meth1()
sc2.meth2()    # 88
sc2.methb()    # 89

print(sc1.__dict__)    # {'_C1__X': 88, '_C2__X': 89}
print(sc2.__dict__)    # {'_C2__X': 89, '_C1__X': 88}




