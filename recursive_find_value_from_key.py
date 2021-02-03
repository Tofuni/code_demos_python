def recursive_find_key_value(x, y):
	if not isinstance(x, dict):
		return None
	for z in x.keys():
		if isinstance(x[z], dict):
			v = recursive_find_key_value(x[z], y)
			if v:
				return v
		if (z == y):
			return x[z]
	return None

# ------------------------- test -------------------------

a = [
	[{"program": {"name": "recursive_program", "language": "python"}, "date": "10/16/20" }, "program"],
	[{"program": {"name": "recursive_program", "language": "python"}, "date": "10/16/20" }, "language"],
	[{"program": {"name": "recursive_program", "language": "python"}, "date": "10/16/20" }, "data"],
	[{"a1": {"a11": 2, "a12": 3},"a2": {"a21": 4, "a22": {"a23": 5}},"a3": 1,}, "a1"],
	[{"a1": {"a11": 2, "a12": 3},"a2": {"a21": 4, "a22": {"a23": 5}},"a3": 1,}, "a11"],
	[{"a1": {"a11": 2, "a12": 3},"a2": {"a21": 4, "a22": {"a23": 5}},"a3": 1,}, "a22"],
	[{"a1": {"a11": 2, "a12": 3},"a2": {"a21": 4, "a22": {"a23": 5}},"a3": 1,}, "a23"],
	[{"a1": {"a11": 2, "a12": 3},"a2": {"a21": 4, "a22": {"a23": 5}},"a3": 1,}, "a3"],
	[{"a1": {"a11": 2, "a12": 3},"a2": {"a21": 4, "a22": {"a23": 5}},"a3": 1,}, "a0"],
	]

for i in a:
	print("\n-----------------\n\n" + str(i[0]) + "\n\n" + "key: " + i[1] + " => value: " + str(recursive_find_key_value(i[0], i[1])))
input()