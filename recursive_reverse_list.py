def recursive_reverse_list(i):
	r = []
	if len(i) <= 1:
		return i
	r = [i[len(i)-1]] + recursive_reverse_list(i[1:len(i)-1]) + [i[0]]
	return r

# ------------------------- test -------------------------

a = [
	[1,2,3],
	[1,2,3,4,5],
	[-10,-8,-6,-4,-2,0,2,4,6,8,10],
	[10,20,30,40],
	[27,94,32,14,88,41,26,90,15,82,72],
	['yi','er','san','si','wu','liu','qi','ba']
	]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n" + str(recursive_reverse_list(i)))
input()