import math

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

# params: (lst) list of numbers, (p) percentage, (t) top/bottom items option
def get_n_vals_percentile(lst, p, t=1, r=1):
	s = sort_list(lst)
	i = {
		0: math.floor(len(lst)*(p/100)),
		1: math.ceil(len(lst)*(p/100)),
		}[r]
	if (t):
		return s[len(s)-1:len(s)-1-i:-1]
	return s[:i]

# ------------------------- test -------------------------

a = [
	[[1,2,3],25],
	[[1,2,3,4,5,6,7,8,9,10],30],
	[[1,2,3,4,5,6,7,8,9,10],30,0],
	[[52,80,33,51,72,34,87,58,14],50],
	[[52,80,33,51,72,34,87,58,14],50,0],
	[[-10,8,-6,4,-2,0],75],
	[[-10,8,-6,4,-2,0],75,0],
	[[1,2,3,4,5,6,7,8,9,10],33,1,1],
	[[1,2,3,4,5,6,7,8,9,10],33,1,0],
	[[-10,8,-6,4,-2,0],75,1,1],
	[[-10,8,-6,4,-2,0],75,1,0]
	]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n" + str(get_n_vals_percentile(*i)))
input()