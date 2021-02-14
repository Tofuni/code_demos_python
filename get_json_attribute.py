import json

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

# params: (fp) path of json file, (attrs) list of attributes to find in json file
def get_json_attrs(fp, attrs=[]):
	try:
		f = open(fp, "r")
		j = json.load(f)
		return [recursive_find_key_value(j, value) for value in attrs]
	except Exception as e:
		print('error for ("' + fp + '", ' + str(attrs) + ') - ' + str(e))

# ------------------------ tests ------------------------
	
tests = [
	get_json_attrs("sample.json"),
	get_json_attrs("sample.json", ['name']),
	get_json_attrs("sample.json", ['name', 'language']),
	get_json_attrs("sample.json", ['valueDNE','date']),
	get_json_attrs("sample.json", ['a1']),
	get_json_attrs("sample.json", ['a22','a23']),
	get_json_attrs("sample.json", ['a3','a0','a1']),
	get_json_attrs("sample.json", ['something']),
]

for test in tests:
	print('\n_________________________\n\n\n' + str(test))

input()