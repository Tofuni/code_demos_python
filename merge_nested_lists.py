def merge_nested_lists(li):
	for a in range(len(li)-1,-1,-1):
		if isinstance(li[a], list):
			b = 0
			for c in li[a]:
				li.insert(a+b,c)
				b+=1
			del li[a+b]
	return li

# ------------------------- test -------------------------

a = [
	[[1,2],[3]],
	[[1,2],[2,4],[3,6]],
	[1,1,[2,2,2],1],
	[1,1,[2,2],1,[3,3,3],[4,4]],
	[[1,2,3],[4,5,6],[7,8,9],['f','l','a','n']],
	[[10,10.5],1,2,3,[],'some',[30],'thing',['po','ta','to'],'hi']
	]

for i in a:
	print('\n' + str(i) + '\n\n' + str(merge_nested_lists(i)) + '\n\n------------------\n')
input()