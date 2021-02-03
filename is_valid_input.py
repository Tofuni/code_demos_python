import re

def is_valid_input(text):
	a = re.search('[^\-\.\w]', text)
	if a == None:
		return True
	return False

# ------------------ test ------------------

tests = [
	"abcDEF",
	"12345",
	"hello world",
	"hello_world",
	"<html>",
	"$USER",
	"2+2",
	"2-2",
	"a=100",
	"ls | cat",
	"SOLAR_sys.tem-2020",
]

for test in tests:
	print(test + "\n")
	print("is_valid_input: " + str(is_valid_input(test)) + "\n\n--------------\n")

input()