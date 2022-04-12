# params: (n) a number
def is_prime(n):
	i = 2
	while(i <= n//i):
		if n%i == 0:
			return {False, "divisible by %i" % i}
		i+=1
	return True

# --------------------------------- test ---------------------------------
	
for a in [7,105,77,127,19,169,719,289,40102392]:
	print(str(a) + " : " + str(is_prime(a)))
input()