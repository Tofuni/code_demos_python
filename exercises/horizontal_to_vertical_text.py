def htov_text(lines):
	max_char = max([len(line) for line in lines])
	r = [[' ' for m in range(len(lines))] for n in range(max_char)]
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			r[j][i] = lines[i][j]
	return r

result = htov_text([
	'doing coursework online',
	'taking naps',
	'watching new shows',
	'coding websites on laptop',
])
for item in result:
	print(item)
input()