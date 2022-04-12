def get_duplicates_and_number_occurances(s):
	d = {}
	for i in s:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	return [[k,v] for k,v in d.items() if v > 1]

tests = [
	[1,2,3,4,5],
	[1,2,2,3,3,3],
	[2,3,1,2,3,4,5,3,1,6,3,2,9],
]
[print(get_duplicates_and_number_occurances(test)) for test in tests]
input()