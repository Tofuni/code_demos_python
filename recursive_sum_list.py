def recursive_sum_list(i):
	r = 0
	if not isinstance(i, list):
		return i
	for ind in range(len(i)):
		if isinstance(i[ind], list):
			nested = recursive_sum_list(i[ind])
			r += nested
		else:
			r += i[ind]
	return r

# ------------------------- test -------------------------

a = [
	[2,2],
	[1,2,3,4],
	[1.2,2.4,3.5,7.2],
	[1,[2,3],4],
	[[1,1,1],[2,2,2],[3,3,3]],
	[[16,80,51],[63,22,15,[50,84],[9,75],71],16],
	[]
	]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n\n" + str(recursive_sum_list(i)))
input()