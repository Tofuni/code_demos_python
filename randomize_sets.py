import random as r

# params: (points) list of items, (num_sets) number of item sets
def randomize_sets(points, num_sets):
	sets = []
	points = points.copy()
	for num in range(num_sets):
		sets.append([])
	while points:
		for set in sets:
			if not points:
				break
			random_index = r.randint(0, len(points)-1)
			set.append(points[random_index])
			del points[random_index]
	return sets

# ----------------------- test -----------------------

args = [
	[[1,2,3,4,5,6,7,8,9], 3],
	[[1,2,3,4,5,6,7,8,9,10,11], 3],
	[['a','b','c','d','e','f','g','h'], 2],
	[[128,534,485,102,658,239,107,386,273,659,239,760,349,658,173,928], 3],
	[['ren','qin','fun','min','tai','kan','rin','zen','xia','liu','wan','kyo','lin','yuu','tsu','cha','sen','nya'],5]
]

for a in range(2):
	print('\ntest ' + str(a+1))
	for arg in args:
		print('\n' + str(arg[0]) + '\n')
		print(str(randomize_sets(*arg)) + '\n\n')
	print('-------------------')

input()