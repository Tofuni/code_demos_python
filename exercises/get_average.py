# params: (lst) list of numbers
def get_average(lst):
	a = 0
	for i in lst:
		a += i
	return a/len(lst)

# ------------------------- test -------------------------

a = [
	[1,2,3,4],
	[0,100],
	[0.5,1.0,1.5,3.0],
	[238,548,391,527,703,810,330,185,272,472,790,832],
	[5]
]
for i in a:
	print("\n" + str(i) + "\naverage: " + str(get_average(i)) + "\n--------------------")
input()