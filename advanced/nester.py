"""嵌套作用域"""
"""在3中可以运行，但2中不行，因为2中method方法看不见类名Spam的"""
def generate():
	class Spam:
		count = 1
		def method(self):
			print(Spam.count)
	return Spam()

generate().method()

"""但即使在3中，method也看不见count，必须是通过self或者Spam才能找到count，比如下面这样会报错：
NameError: name 'count' is not defined
"""

def generate_unfix():
	class Spam:
		count = 1
		def method(self):
			print(count)
	return Spam()

generate_unfix().method()