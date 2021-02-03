def uniq_list(li):
	f = []
	for i in li:
		if not i in f:
			f.append(i)
	return f

# ------------------------- test -------------------------

a = [
	[1,2,2,3,3,3],
	[10,65,32,87,23,76,10,53,65,87,10]
	]
for i in a:
	print('\n' + str(i) + '\n' + str(uniq_list(i)) + '\n\n----------------------------')
input()