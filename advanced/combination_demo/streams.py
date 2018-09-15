class Processor:
	"""组合：Processor是容器，reader和writer是嵌入其中的对象，Processor的process方法的实现依靠这些对象和方法
	继承：但是Processor的conventer方法还没有实现，所以需要子类继承后实现"""
	def __init__(self, reader, writer):
		self.reader = reader
		self.writer = writer
	def process(self):
		while True:
			data = self.reader.readline()
			if not data:
				break
			data = self.conventer(data)
			self.writer.write(data)
	def conventer(self, data):
		assert False, "conventer must be defined"


if __name__ == "__main__":
	import sys
	processor = Processor(open("employee.py"), sys.stdout)
	processor.process()