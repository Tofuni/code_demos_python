# params: (lst) list of items
def is_elems_same_type(lst):
	if len(lst) > 1:
		t = type(lst[0])
		for e in lst[1:]:
			if t != type(e):
				return False
		return True
	return None

# ---------------------- test ---------------------

tests = [
	[1,2,3,4],
	[1,2,'three',4],
	[1,[2],3,4],
	[[1],[2],[3],[4]],
	['one','two','three','four'],
	[1,2,3.0,4],
	[1.6,3.3,5.2,10.62],
	[]
]

for test in tests:
	print(f"{test}\n\nelems same type: {is_elems_same_type(test)}\n-------------------------\n")

input()