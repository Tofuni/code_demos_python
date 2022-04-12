# params: (i) list of numbers
def recursive_sort_list_two_tailed(i):
	r = []
	if len(i) <= 1:
		return i
	for j in range(len(i)):
		if i[j] < i[0]:
			i[0], i[j] = i[j], i[0]
		if i[j] > i[-1]:
			i[-1], i[j] = i[j], i[-1]
	r += [i[0]] + recursive_sort_list_two_tailed(i[1:-1]) + [i[-1]]
	return r

# ------------------------- test -------------------------

a = [
	[3,2,1],
	[10,8,6,4,2,0],
	[1,-2,3,-4,5,-6,7,-8,9,-10],
	[27,94,32,14,88,41,26,90,15,82,72],
	[1,2,3,4,5],
	[0.6,1.9,0.7,4.2,7.6,1.9,3.6,0.2,8.0,3.7,5.8]
	]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n" + str(recursive_sort_list_two_tailed(i)))
input()