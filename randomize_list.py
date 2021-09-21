import random as r

# params: (li) list of items
def randomize(li):
	a = []
	list = li.copy()
	for e in range(0, len(list)):
		i = r.randint(0, len(list)-1)
		a.append(list[i])
		del list[i]
	return a

# ------------------------- test -------------------------
	
a = [
	[1,2,3,4,5,6,7,8,9,10],
	[1,2,3,4,5,6,7,8,9,10],
	[1,2,3,4,5,6,7,8,9,10],
	[1,2,3,4,5,6,7,8,9,10],
	[1,2,3,4,5,6,7,8,9,10],
	]
for i in a:
	print('\n' + str(randomize(i)))
input()