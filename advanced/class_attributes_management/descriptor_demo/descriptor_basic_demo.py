
"""
class Descriptor:
    "docstring goes here"
    def __get__(self, instance, owner): ...
         # Return attr value
    def __set__(self, instance, value): ...
         # Return nothing (None)
    def __delete__(self, instance): ...
         # Return nothing (None)
带有任何这些方法的类都可以看作是描述符，描述符的实例可以作为其他的类的属性的值。
这样，当访问或者想要操作其他类中的这些属性时，会自动调用描述符中的对应方法。
特性实际上也只是创建一种特定描述符的方便方法。
如果有个方法比如__set__空缺，并不意味着不允许set操作。真正做到不允许set操作的正确方法是——定义__set__方法并在其中引发异常

"""
class Descriptor(object):
	def __get__(self, instance, owner):
		print(self, instance, owner, sep='\n')

class Subject:
	attr = Descriptor() # Descriptor instance is class attr


X = Subject()
print("X.attr", X.attr)
print()
print("Subject.attr", Subject.attr)
print()

"""当一个描述符类在客户类之外无用的话，将描述符的定义嵌入客户类之
中，这在语法上是完全合理的"""
class Person:
	def __init__(self, name):
		self._name = name
	class Name: # Using a nested class
		"name descriptor docs"
		def __get__(self, instance, owner):
			print('fetch...')
			return instance._name
		def __set__(self, instance, value):
			print('change...')
			instance._name = value
		def __delete__(self, instance):
			print('remove...')
			del instance._name
	name = Name()

grace = Person("grace")
print(grace.name)
grace.name = "grace2"
print(grace.name)
print(grace.Name.__doc__)  #而不再是Name.__doc__