# params: (n) number in the sequence
def fibonacci_number(n):
	if n <= 1:
		return n
	previous2 = 0
	previous1 = 1
	current = None
	for a in range(1,n):
		current = previous1 + previous2
		previous2 = previous1
		previous1 = current
	return current

# ------------------------- test -------------------------

a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in a:
	print("\n\nfibonacci_number(" + str(i) + ") = " + str(fibonacci_number(i)))
input()