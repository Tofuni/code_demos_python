# params: (s) string, (x) substring to get indices of in string

# soln 1
def get_indices_of_x_in_string(s, x):
	r = []
	a = 0
	while (True):
		b = s.find(x)
		if  b != -1:
			a += b
			r.append(a)
			s, a = s[s.find(x)+1:], a+1
		else:
			break
	return r
	
# soln 2
def get_indices_of_x_in_string_2(s, x):
	r = []
	for a in range(len(s)-len(x)+1):
		if s[a:a+len(x)] == x:
			r.append(a)
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
	print(str(test[0]) + " --- " + str(test[1]) + "\n\nindices (solution_1): " + str(get_indices_of_x_in_string(*test)) + "\n\n--------------\n")
	print(str(test[0]) + " --- " + str(test[1]) + "\n\nindices (solution 2): " + str(get_indices_of_x_in_string_2(*test)) + "\n\n--------------\n")

input()