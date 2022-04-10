def pair_sum(n, s):
	pairs = []
	for i in range(len(s)):
		for j in s[i+1::]:
			if s[i] + j == n:
				pairs.append([s[i], j])
	return pairs

results = [
	pair_sum(3, [1,2,3,4,5,6,7,8,9,10]),
	pair_sum(6, [1,2,3,4,5,6,7,8,9,10]),
	pair_sum(10, [1,2,3,4,5,6,7,8,9,10]),
	pair_sum(15, [1,2,3,4,5,6,7,8,9,10])
]
[print(r) for r in results]
input()