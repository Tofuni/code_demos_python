def longest_uniq_substr(s):
	if len(s) == 0:
		return s
	c = {}
	for idx in range(0, len(s)):
		c[idx] = s[idx]
	for i in c.keys():
		for j in range(i, len(s)-1):
			if s[j+1] in c[i]:
				break
			c[i] += s[j+1]
	max_len = max([len(k) for k in c.values()])
	for a in c.values():
		if len(a) == max_len:
			return a
	return ""

tests = [
	"abo33wnrre43iifbnla3wo",
	"abcdefghijklmnop",
	"12345512334567876545678987654322",
	"zzzzz",
	"12123123412345123412345612312123451231",
	"one two three four five six seven eight nine ten",
	"onetwothreefivesixseveneightnineten",
	"this is an example sentence to test finding a unique substring sequence for a string input",
	"thisisanexamplesentencetotestfindingauniquesubstringsequenceforastringinput",
	"s",
	""
]
[print(longest_uniq_substr(test)) for test in tests]
input()
