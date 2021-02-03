def get_elems_greater_less_than(lst, num, s):
	return {
		'>': [i for i in lst if i > num],
		'<': [i for i in lst if i < num]
	}[s]

# ---------------------- test ---------------------

tests = [
	[[1,2,3,4,5,6,7,8,9,10], 3],
	[[1,2,3,4,5,6,7,8,9,10], 5],
	[[1,2,3,4,5,6,7,8,9,10], 10],
	[[73,29,76,10,38,58,22,17,45,31,84,37,60,39,75,55,16], 30]
]

print("\ntest get_elems_greater_than(lst, num, '>')\n\n")
for test in tests:
	print(f"{test[0]} --- greater than {test[1]}\n\n{get_elems_greater_less_than(*test, '>')}\n-------------------------\n")

print("\n\ntest get_elems_less_than(lst, num, '<')\n\n")
for test in tests:
	print(f"{test[0]} --- less than {test[1]}\n\n{get_elems_greater_less_than(*test, '<')}\n-------------------------\n")

input()