# params: (m1) a 2d matrix, (m2) a 2d matrix with the same dimensions as m1
def sum_matrices(m1, m2):
	r = m1.copy()
	for i in range(len(m1)):
		for j in range(len(m1[0])):
			r[i][j] += m2[i][j]
	return r

# ------------------------- test -------------------------

a = [
	[
		[
			[1,2],
			[3,4]
		],
		[
			[2,4],
			[3,6]
		]
	],
	[
		[
			[1,2,3],
			[4,5,6],
			[7,8,9]
		],
		[
			[10,20,30],
			[40,50,60],
			[70,80,90]
		]
	],
	[
		[
			[21,68,32,75],
			[10,95,41,21],
			[72,15,56,62]
		],
		[
			[64,29,51,23],
			[22,81,12,76],
			[53,97,90,58]
		]
	],
	[
		[
			[17,8,1,19,4,7,2],
			[14,16,3,9,0,15,5]
		],
		[
			[10,7,15,18,2,6,3],
			[16,11,9,14,12,0,19]
		]
	]
]
for i in a:
	print("\nmatrices to add:\n")
	for row in i[0]:
		print(row)
	print("\n")
	for row in i[1]:
		print(row)
	r = sum_matrices(*i)
	print("\nsummed matrices:\n")
	for row in r:
		print(row)
	print("\n-----------------\n")
input()