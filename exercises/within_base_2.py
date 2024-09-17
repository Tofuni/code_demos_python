def within_base_2(num):
	i = 0
	while True:
		if num > 2**i:
			i+=1
		else:
			break
	return i

tests = [
	1,
	10,
	12345,
	67345827,
	22054275169038467438,
	2,
	4,
	8,
	15,
	16,
	17
]
[print("input: " + str(test )+ "\noutput: (" + str(within_base_2(test)) + ")\n2**" + str(within_base_2(test)) + " = " + str(2**within_base_2(test)) + "\n") for test in tests]
input()