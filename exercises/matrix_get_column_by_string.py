# params: (matrix) 2d array, (text) string to query a column
def get_column_by_string(matrix, text):
	col = []
	if text not in matrix[0]:
		return None
	index = matrix[0].index(text)
	for row in matrix:
		col.append(row[index])
	return col

# ------------------------- test -------------------------

a = [['a','b','c','d','e','f','g','h'],
	[1,2,3,4,5,6,7,8],
	[9,10,11,12,13,14,15,16],
	[17,18,19,20,21,22,23,24],
	[25,26,27,28,29,30,31,32]]
indices = ['a','d','g','b','e','h','c','f','i','j']

print("\nmatrix\n")
for i in a:
	print(str(i))
print("\n\n------------------------------")
for index in indices:
	print("\nstring - " + str(index) + "\ncolumn - " + str(get_column_by_string(a, index)))
input()