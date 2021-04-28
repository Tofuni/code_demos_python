def spiral_matrix(matrix):
	a = []
	t = 0
	r = len(matrix[0])-1
	b = len(matrix)-1
	l = 0
	iter = 0
	num_matrix_items = len(matrix[0])*len(matrix)

	for x in range(0,(len(matrix)//2)+1):
		if (len(a) >= num_matrix_items-1):
			if len(a) != num_matrix_items:
				a.append(matrix[t][0+iter])
			break
		for item in matrix[t][0+iter:-1-iter]:
			a.append(item)
		if (len(a) >= num_matrix_items-1):
			if len(a) != num_matrix_items:
				a.append(matrix[0+iter][r])
			break
		for row in matrix[0+iter:-1-iter]:
			a.append(row[r])
		if (len(a) >= num_matrix_items-1):
			if len(a) != num_matrix_items:
				a.append(matrix[b][len(matrix[b])-iter-1])
			break
		for item in reversed(matrix[b][1+iter:len(matrix[b])-iter]):
			a.append(item)
		if (len(a) >= num_matrix_items-1):
			if len(a) != num_matrix_items:
				a.append(matrix[len(matrix)-iter-1][l])
			break
		for row in reversed(matrix[1+iter:len(matrix)-iter]):
			a.append(row[l])

		t += 1
		r -= 1
		b -= 1
		l += 1
		iter += 1
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
	[21,22,23,24]
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