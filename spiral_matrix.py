# params: (matrix) a 2d matrix
def spiral_matrix(matrix):
	a = []
	top = 0
	right = len(matrix[0])-1
	bottom = len(matrix)-1
	left = 0
	iteration = 0
	num_matrix_items = len(matrix[0])*len(matrix)

	for x in range(0,(len(matrix)//2)+1):
		# top
		if (len(a) >= num_matrix_items-1):
			if len(a) != num_matrix_items:
				a.append(matrix[top][iteration])
			break
		for item in matrix[top][iteration:-1-iteration]:
			a.append(item)
		# right
		if (len(a) >= num_matrix_items-1):
			if len(a) != num_matrix_items:
				a.append(matrix[iteration][right])
			break
		for row in matrix[iteration:-1-iteration]:
			a.append(row[right])
		# bottom
		if (len(a) >= num_matrix_items-1):
			if len(a) != num_matrix_items:
				a.append(matrix[bottom][len(matrix[bottom])-1-iteration])
			break
		for item in reversed(matrix[bottom][1+iteration:len(matrix[bottom])-iteration]):
			a.append(item)
		# left
		if (len(a) >= num_matrix_items-1):
			if len(a) != num_matrix_items:
				a.append(matrix[len(matrix)-1-iteration][left])
			break
		for row in reversed(matrix[1+iteration:len(matrix)-iteration]):
			a.append(row[left])
		# iterate
		top += 1
		right -= 1
		bottom -= 1
		left += 1
		iteration += 1
	return a

# ------------------------- test -------------------------

m1 = [
    [1,2],
	[3,4]
]
print("\nmatrix: ")
for i in m1:
	print(str(i))
print("\nspiral form: " + str(spiral_matrix(m1)) + "\n\n-----\n")

m2 = [
    [1,2,3],
	[4,5,6],
	[7,8,9]
]
print("\nmatrix: ")
for i in m2:
	print(str(i))
print("\nspiral form: " + str(spiral_matrix(m2)) + "\n\n-----\n")

m4 = [
    [1,2,3,4,5,6],
	[7,8,9,10,11,12],
	[13,14,15,16,17,18],
	[19,20,21,22,23,24],
]
print("\nmatrix: ")
for i in m4:
	print(str(i))
print("\nspiral form: " + str(spiral_matrix(m4)) + "\n\n-----\n")

m2 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
print("\nmatrix: ")
for i in m2:
	print(str(i))
print("\nspiral form: " + str(spiral_matrix(m2)) + "\n\n-----\n")

m3 = [
    [1,2,3,4,5,6,7,8],
    [9,10,11,12,13,14,15,16],
	[17,18,19,20,21,22,23,24],
	[25,26,27,28,29,30,31,32],
	[33,34,35,36,37,38,39,40],
]
print("\nmatrix: ")
for i in m3:
	print(str(i))
print("\nspiral form: " + str(spiral_matrix(m3)) + "\n\n-----\n")

m4 = [
    [1,2,3,4],
    [5,6,7,8],
	[9,10,11,12],
	[13,14,15,16],
	[17,18,19,20],
	[21,22,23,24],
	[25,26,27,28]
]
print("\nmatrix: ")
for i in m4:
	print(str(i))
print("\nspiral form: " + str(spiral_matrix(m4)) + "\n\n-----\n")

m5 = [
    [1,2,3],
    [4,5,6],
	[7,8,9],
	[10,11,12],
	[13,14,15],
]
print("\nmatrix: ")
for i in m5:
	print(str(i))
print("\nspiral form: " + str(spiral_matrix(m5)) + "\n\n-----\n")

m5 = [
    [1,2,3,4],
    [5,6,7,8],
	[9,10,11,12],
	[13,14,15,16],
	[17,18,19,20],
]
print("\nmatrix: ")
for i in m5:
	print(str(i))
print("\nspiral form: " + str(spiral_matrix(m5)) + "\n\n-----\n")

input()