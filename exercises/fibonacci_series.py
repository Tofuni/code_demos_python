# params: (n) number in the sequence
def fibonacci_series(n):
	if n <= 1:
		return list(range(n+1))
	previous2 = 0
	previous1 = 1
	current = None
	r = [0,1]
	for a in range(1,n):
		current = previous1 + previous2
		r.append(current)
		previous2 = previous1
		previous1 = current
	return r

# ------------------------- test -------------------------

a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in a:
	print("\n\nfibonacci_series(" + str(i) + ") = " + str(fibonacci_series(i)))
input()