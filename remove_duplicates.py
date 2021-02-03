def sort_list(ls):
	b = 1
	while b != 0:
		b = 0
		for a in range(0,len(ls)-1):
			if ls[a] > ls[a+1]:
				ls[a], ls[a+1] = ls[a+1], ls[a]
				b += 1
	return ls

def remove_duplicates(arr):
	arr = sort_list(arr)
	for i in range(len(arr)-1,0,-1):
		if arr[i] == arr[i-1]:
			del arr[i]
	return arr
	
# ------------------------- test -------------------------

a = [
	[1,1,1,1,1],
	[1,1,2,2,3,3],
	[5,4,3,2,1,0,1,2,3,4,5],
	[1,3,5,7,7,9,9,10,10,12,12,12,16,19,20,22,22,35,36,39,39,39],
	[10,2,6,8,1,2,5,7,9,6,7,8,0,5,6,9,0,10,2,6,7,8,1,5,7,9,10,1],
	]

for i in a:
	print('\n' + str(i) + '\n\n' + str(remove_duplicates(i)) + '\n\n------------------\n')
input()