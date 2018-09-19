"""A pizzashop is a container containing Server, chef, oven, and costomer"""
from employee import PizzaRobot, Server

class Customer:
	def __init__(self, name):
		self.name = name
	def order(self, server):
		print(self.name, "orders from", server)
	def pay(self, server):
		print(self.name, "pays for item to", server)

class Oven:
	def bake(self):
		print("oven bakes")

class PizzaShop:
	"""a container"""
	def __init__(self):
		self.server = Server("pat")
		self.chef = PizzaRobot("Bob")
		self.oven = Oven()

	def order(self, name):
		"""组合：这是新的接口order，不过它的实现依赖了其中的对象以及它们的方法"""
		customer = Customer(name)
		customer.order(self.server)
		self.chef.work()
		self.oven.bake()
		customer.pay(self.server)


if __name__ == "__main__":
	scene = PizzaShop()
	scene.order("Homer")
	print("")
	scene.order("Shaggy")