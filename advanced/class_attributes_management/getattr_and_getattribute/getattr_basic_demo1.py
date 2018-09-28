"""使用未定义的属性，会触发getattr"""
class Catcher:
	def __getattr__(self, name):
		print('Get:', name)
	def __setattr__(self, name, value):
		print('Set:', name, value)

X = Catcher()
X.job # Prints "Get: job"
X.pay # Prints "Get: pay"
X.pay = 99 # Prints "Set: pay 99"



"""getattr用于委托"""
class Wrapper:
	"""实现对object行为的跟踪"""
	def __init__(self, object):
		self.wrapped = object # Save object
	def __getattr__(self, attrname):
		print('Trace:', attrname) # Trace fetch
		return getattr(self.wrapped, attrname) # Delegate fetch


l = Wrapper([1,2,3,4])
l.pop(3)
print(l.count(4))
