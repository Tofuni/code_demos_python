import random

# params: (li) a list of items
def pop_random(li):
	i = random.randint(0, len(li)-1)
	d = li[i]
	del(li[i])
	return d

# ------------------------- test -------------------------

a = [
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9]
]
for i in a:
	r = pop_random(i)
	print("\n-----------------\n\nupdated list: " + str(i) + "\nremoved item: " + str(r))
input()