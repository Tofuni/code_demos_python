import timeit

def test_timer(size=100):
	obj = {}
	for a in range(size):
		obj[str(a)]=a*2
	return

# params: (func) function call, (setup_func) function name, (number) number of runtimes, (repeat) number of repeat times
def time_func(func, setup_func, number=1000, repeat=1):
	setup = "from __main__ import " + setup_func
	if repeat > 1:
		result = timeit.repeat(func, setup, number=number, repeat=repeat)
		result.append({'fastest run': min(result)})
	else:
		result = timeit.timeit(func, setup, number=number)
	return result

# ----------------------- test -----------------------

tests = [
	["test_timer()", "test_timer"],
	["test_timer(10000)", "test_timer", 10000],
	["test_timer(20000)", "test_timer", 10000],
	["test_timer(1000)", "test_timer", 10],
	["test_timer(1000)", "test_timer", 100],
	["test_timer(1000)", "test_timer", 1000],
	["test_timer(1000)", "test_timer", 1000, 2],
	["test_timer(1000)", "test_timer", 1000, 5],
	["test_timer(1000)", "test_timer", 1000, 10]
]

for test in tests:
	print('\n' + str(test) + '\n\n' + str(time_func(*test)) \
	+ '\n\n--------------------------------------------')

input()