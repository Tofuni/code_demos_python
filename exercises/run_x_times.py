import datetime as dt

def hello():
	print('hello worlds')
	return

def printTime():
	print(dt.datetime.now())
	return

def testArgs(arg1, arg2, arg3, arg4):
	print(arg1 + ' ' + arg2)
	print(arg3['key'] + ' ' + str(arg4) + '\n')
	return

# -------------------- run_x_times --------------------

# params: (func) function name, (args) list of arguments, (x) number of runtimes
def run_x_times(func, args=[], x=1):
	for a in range(x):
		func(*args)

# --------------------- test ---------------------

test_args = [
	[hello, [], 2],
	[hello, [], 10],
	[hello],
	[printTime, [], 3],
	[testArgs, ['hi','panda',{'key':'value'},3.1], 5],
]

for test in test_args:
	run_x_times(*test)
	print('\n-------------------------\n')

input()