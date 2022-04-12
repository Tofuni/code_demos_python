# params: (matrix) 2d array, (index) an integer index
def get_column_by_index(matrix, index):
	col = []
	if index not in range(len(matrix[0])):
		return None
	for row in matrix:
		col.append(row[index])
	return col

# ------------------------- test -------------------------

a = [['a','b','c','d','e','f','g','h'],
	[1,2,3,4,5,6,7,8],
	[9,10,11,12,13,14,15,16],
	[17,18,19,20,21,22,23,24],
	[25,26,27,28,29,30,31,32]]
indices = [0,2,4,6,1,3,5,7,9]

print("\nmatrix\n")
for i in a:
	print(str(i))
print("\n\n------------------------------")
for index in indices:
	print("\nindex - " + str(index) + "\ncolumn - " + str(get_column_by_index(a, index)))
input()