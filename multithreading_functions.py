import threading

def calculation(repeats, test_name):
	r = 10000000
	for a in range(repeats):
		r += a**0.5
	print("\n--------------------\n" + test_name + " has finished! \n--------------------\n")
	return r

def example_obj(test_name):
	d = {}
	for a in range(3000000):
		d[str(a)] = a*3
	print("\n--------------------\n" + test_name + " has finished! \n--------------------\n")
	return d

def limit(upper_bound, test_name):
	a = 1
	while a < upper_bound:
		a+=1
	print("\n--------------------\n" + test_name + " has finished! \n--------------------\n")
	return a

# --------------------- threading_functions ---------------------

def multithreading_functions(inputs):
	for input in inputs:
		t = threading.Thread(target=input["function"], args=(*input["args"],))
		t.start()
		print(str(t) + " \nstarting function " + input["function"].__name__ + \
		" with args " + str(input["args"]) + "\n")

# ------------------------- test -------------------------

inputs = [
	{"function": calculation, "args":[200000, "test_1 - calculation(200000)"]},
	{"function": calculation, "args":[5000000, "test_2 - calculation(5000000)"]},
	{"function": example_obj, "args":["test_3 - example_obj()"]},
	{"function": limit, "args":[10000000, "test_4 - limit(10000000)"]},
	{"function": limit, "args":[100000, "test_5 - limit(100000)"]}
]

multithreading_functions(inputs)

input()