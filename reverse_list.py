def reverse_list(li):
	i, h = len(li)-1, len(li)//2
	for j in range(h):
		li[j], li[i-j] = li[i-j], li[j]
	return li
	
# ------------------- test -------------------

tests = [
	[1],
	[0],
	[1,2],
	[1,2,3],
	[1,2,3,4,5],
	[5,4,3,2,1],
	[1,2,3,4,5,6,7,8,9,10],
	[103,428,76,196,81,768,209,38],
	['apricot','banana','cantaloupe','durian','elderberry']
]

for test in tests:
	print('\n' + str(test) + '\n')
	print('\n' + str(reverse_list(test)) + '\n\n---------------------')

input()