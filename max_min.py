def min_max(list):
	r = [list[0]]
	for e in range(1,len(list)):
		if list[e] > r[-1]:
			r.append(list[e])
		elif list[e] < r[0]:
			r.insert(0, list[e])
	return {"max": r[-1], "min": r[0]}

# ------------------------- test -------------------------

a = [
	[34,75,234,768,3,476,1053,367,86,12,5,87,3452,15,3460,23,645,2330],
	[1,3,5,7,9,0,2,4,6,8],
	[-100,-23,-457,41,7695,-23,7560,123,5786,12,654,-2304,129,540,34,659]
	]
for i in a:
	print("\n" + str(i) + "\n" + str(min_max(i)))
input()