# params: (i) list of items
def recursive_flatten_list(i):
	r = []
	if not isinstance(i, list):
		return i
	for a in i:
		if isinstance(a, list):
			b = recursive_flatten_list(a)
			for c in b:
				r.append(c)
		else:
			r.append(a)
	return r

# ------------------------- test -------------------------

a = [
	[1,2,3,4],
	[1,[2],[3,4]],
	[1,[2,3],[[4,5],6,[7,8,9,10]]],
	[1,[2,3],7,[4,5,6,[1,2,3]],8],
	[],
	]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n\n" + str(recursive_flatten_list(i)))
input()