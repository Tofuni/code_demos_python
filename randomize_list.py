import random as r

def randomize(li):
	a = []
	for e in range(0, len(li)):
		i = r.randint(0, len(li)-1)
		a.append(li[i])
		del li[i]
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