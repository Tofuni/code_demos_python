import random

def get_item_locals(item, items, span):
	r = []
	for i in range(len(items)):
		if items[i] == item:
			start = i-span
			end = i+span+1
			if start < 0:
				start = 0
			if end > len(items):
				end = len(items)
			r.append(items[start:end])
	return r

tests = [
	[5, [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1], 2],
	[1, [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1], 2],
	[2, [random.randint(0,9) for i in range(50)], 1],
	[2, [random.randint(0,9) for i in range(50)], 2]
]
for test in tests:
	print(str(test[1]) + "\n\n" + str(get_item_locals(test[0], test[1], test[2])) + "\n\n------------\n")
input()