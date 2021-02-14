# params: (i) a list
def item_frequency(i):
	a = {}
	for b in i:
		a[str(b)] = 1 if str(b) not in a.keys() else a.get(str(b))+1
	return a

# ------------------------- test -------------------------
			
a = [
	[0,1,2,3,4],
	[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5],
	[15,67,34,79,28,61,23,75,23,65,41,36,76,39,10,15,54,23,10,27,84,28,61,65,41],
	['a','b','c','d','e','c','a'],
	'this is a honeycrisp apple and that is a fuji apple'.split(' '),
	]
for i in a:
	print('\n' + str(i) + '\n\n' + str(item_frequency(i)) + '\n\n----------------------------------')
input()