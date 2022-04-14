def max_diff_in_list_rl(s):
	max_diff = 0
	idxs = [0,0]
	for i in range(len(s)):
		for j in range(i+1, len(s)):
			if s[j]-s[i] > max_diff:
				max_diff = s[j]-s[i]
				idxs = [i,j]
	return idxs

print(max_diff_in_list_rl([10,8,16,6,11,15,9]))
input()