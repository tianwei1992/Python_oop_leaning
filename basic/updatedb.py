"""Update Person object on database
Here，giveRaise to the pay of a once run
"""

import shelve
db = shelve.open("persondb")
a = db["a"]
a.giveRaise(.10)
db["a"] = a
db.close()
print(a)