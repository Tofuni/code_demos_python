# params: (a1) a list, (a2) a list, (i) a numeric index of list a2
def merge_lists(a1,a2,i):
	if i <= len(a2) and i >= 0:
		b = 0
		for a in a1:
			a2.insert(i+b,a)
			b+=1
		return a2
	return None
	
# ------------------------- test -------------------------

a = [
	[[1,1,1],[2,2,2],0],
	[[4,5,6],[1,2,3],2],
	[[4,5,6],[1,2,3],3],
	[[10,5,0,-5],[6,5,4,3,2,1,0,-1,-2,-3,-4,-5],8],
	[[239,645,239,604,961,200],[238,658,128,598,450,462],2],
	[[1,1,1],[2,2,2],4],
	]

for i in a:
	print('\n' + str(i[0]) + '\n' + str(i[1]) + '\n\nmerge at index: ' + str(i[2]) + '\n\n' \
	+ str(merge_lists(i[0],i[1],i[2])) + '\n\n------------------\n')
input()