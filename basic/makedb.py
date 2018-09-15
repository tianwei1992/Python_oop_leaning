"""Store objects on a shelve database"""

from person import Person, Manager
a = Person("a", "worker", 10)
b = Person("b", "worker", 20)
c = Manager("c", 50)

import shelve
db = shelve.open('persondb')
for object in [a, b, c]:
	db[object.name] = object
db.close()