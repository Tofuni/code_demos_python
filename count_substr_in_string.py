# params: (s) string, (x) substring to count in string

# soln 1
def x_count_in_string(s, x):
	r = 0
	while (True):
		if s.find(x) != -1:
			r += 1
			s = s[s.find(x)+1:]
		else:
			break
	return r
	
# soln 2
def x_count_in_string_2(s, x):
	r = 0
	for a in range(len(s)-len(x)+1):
		if s[a:a+len(x)] == x:
			r += 1
	return r

# ------------------ test ------------------

tests = [
	["fuji apples, honeycrisp apples, green apples, kanzi apples, gala apples","apples"],
	["1689234581356873465870234021347586413217","58"],
	["agoiandwenogandfklgmzamdjoitandgnexupi","and"],
	["bananas","na"],
	["rune, rule, and ruse are words starting with ru", "ru"]
]

for test in tests:
	print(str(test[0]) + " --- " + str(test[1]) + "\n\ncount (solution_1): " + str(x_count_in_string(*test)) + "\n\n--------------\n")
	print(str(test[0]) + " --- " + str(test[1]) + "\n\ncount (solution 2): " + str(x_count_in_string_2(*test)) + "\n\n--------------\n")

input()