# params: (ls) list of numbers
def sort_list(ls):
	b = 1
	while b:
		b = 0
		for a in range(0,len(ls)-1):
			if ls[a] > ls[a+1]:
				ls[a], ls[a+1] = ls[a+1], ls[a]
				b = 1
	return ls

# params: (lst) list of numbers, (n) number of items to get, (t) top/bottom items option
def get_n_vals(lst, n, t=1):
	s = sort_list(lst)
	if (t):
		return s[len(s)-1:len(s)-1-n:-1]
	return s[:n]

# ------------------------- test -------------------------

a = [
	[[1,2,3],2],
	[[1,2,3,4,5,6,7,8,9,10],3],
	[[1,2,3,4,5,6,7,8,9,10],3,0],
	[[52,80,33,51,72,34,87,58,14],5],
	[[52,80,33,51,72,34,87,58,14],5,0],
	[[-10,8,-6,4,-2,0],3],
	[[-10,8,-6,4,-2,0],3,0]
	]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n" + str(get_n_vals(*i)))
input()