"""demonstrates combination of classes
class Person and Manager are both embeded in class Department.
"""
from basic.person import Person, Manager

a = Person('a', 'worker', 10)
b = Person('b', 'worker', 0)
c = Manager('c', 50)

class Department:
	def __init__(self, *args):
		self.members = list(args)
	def addMember(self, person):
		self.members.append(person)
	def giveRaises(self, percent):
		for person in self.members:
			person.giveRaise(percent)
	def showAll(self):
		for person in self.members:
			print(person)


if __name__ == "__main__":
	development = Department(a,b)
	development.addMember(c)
	development.giveRaises(.10)
	development.showAll()