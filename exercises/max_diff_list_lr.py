def max_diff_in_list_lr(s):
	max_diff = 0
	idxs = [0,0]
	for i in range(len(s)):
		for j in range(i+1, len(s)):
			if s[i]-s[j] > max_diff:
				max_diff = s[i]-s[j]
				idxs = [i,j]
	return idxs

print(max_diff_in_list_lr([10,8,16,6,11,15,9]))
input()