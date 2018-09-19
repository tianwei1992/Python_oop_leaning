from streams import Processor
"""Processor是一个抽象超类，因为conventer方法待实现"""

class Uppercase(Processor):
	"""实现了conventer，相当于定制了特定conventer的Processor"""
	def conventer(self, data):
		return data.upper()

if __name__ == "__main__":
	import sys
	obj = Uppercase(open("employee.py"), sys.stdout)
	obj.process()
