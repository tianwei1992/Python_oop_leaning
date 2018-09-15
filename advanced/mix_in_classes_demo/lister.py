class ListInstance:
	"""A Mix-in class
	Provides formatted print() or str() of instances via inheritance of __str__
	Displays instance infos and its attrs"""
	def __str__(self):
		return '<Instance of {}. address:{} \n {}'.format(self.__class__.__name__,
														  id(self),
														  self.__attrnames())
	def __attrnames(self):
		result = ""
		for attr in sorted(self.__dict__):
			result += "\tname {}={}\n".format(attr, self.__dict__[attr])
		return result

class ListInherited:
	"""A Mix-in class, too.
	Diffefencee from class ListInstance:
	    Providing more attrs using dir rather than __dict__
	Note:
		For attrs staring with '__' , getattr is ommited """
	def __str__(self):
		return '<Instance of {}. address:{} \n {}'.format(self.__class__.__name__,
														  id(self),
														  self.__attrnames())
	def __attrnames(self):
		result = ""
		for attr in dir(self):
			if attr[:2] =="__":
				result += "\tname {}=<>\n".format(attr)
			else:
				result += "\tname {}={}\n".format(attr, getattr(self, attr))
		return result

class ListTree:
	"""A Mix-in class, too,more advanced.
	Diffefencee from class ListInherited:
	    Providing attrs with where the inheritance from
	Note:
		For attrs staring with '__' , getattr is ommited """

	def __str__(self):
		self.__visited = {}
		return '<Instance of {0}. address:{1} \n {2}{3}'.format(
			self.__class__.__name__,
			id(self),
			self.__attrnames(self, 0),
			self.__listclass(self.__class__, 4))    #b不仅列出自己当前的attrs，还要往上追溯父类的attrs，每次往上一级多缩进4格
	def __listclass(self, aClass, indent):
		"""用递归思想实现遍历所有父类的attrs，直到继承数的顶端"""
		dots = "." * indent
		if aClass in self.__visited:
			"""如果已经访问过，不再重复打印。"""
			return '\n{0}<Class {1}:, address {2}:(see above)>\n'.format(
				dots,
				aClass.__name__,
				id(aClass))
		else:
			self.__visited[aClass] = True
			genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
			return '\n{0}<Class {1}:, address {2}:\n{3}{4}{5}>\n'.format(
				dots,
				aClass.__name__,
				id(aClass),
				self.__attrnames(aClass, indent),    # 首先打印当前aClass的信息
				''.join(genabove),    # 再打印往上的信息
				dots)

	def __attrnames(self, obj, indent):
		spaces = " " * (indent + 4)
		result = ""
		for attr in sorted(obj.__dict__):
			if attr.startswith("__") and attr.endswith("__"):
				result += spaces + "{0}=<>\n".format(attr)
			else:
				result += spaces + "{0}={1}\n".format(attr, getattr(obj, attr))
		return result

