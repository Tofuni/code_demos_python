import re

def numbers_and_letters(s):
	ltr_check = re.compile('[a-zA-Z]')
	num_check = re.compile('[0-9]')
	result = {
		"letters": "",
		"numbers": "",
		"other": ""
	}
	for chr in s:
		if ltr_check.match(chr):
			result["letters"] += chr
		elif num_check.match(chr):
			result["numbers"] += chr
		else:
			result["other"] += chr
	return result

tests = [
	"Example Test",
	"abcde@12345_FGHIJ",
	"5 km / 23:03 min",
	"current goals for running are improving 5k and 10k times",
	"1hr language study - 950 days streak progress: 918/950",
]
[print("input: " + test + "\noutput: " + str(numbers_and_letters(test)) + "\n") for test in tests]
input()