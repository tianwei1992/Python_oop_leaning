"""read Person objects on a shlve database"""

import shelve
db = shelve.open("persondb")
print(len(db))
print(list(db.keys()))
for key in db:
	print("{}->{}".format(key, db[key]))
print(db["a"].lastName())