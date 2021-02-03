def matrix_form(matrix, placeholder):
	max_row = 0
	m = []
	for row in matrix:
		if len(row) > max_row:
			max_row = len(row)
	for row in matrix:
		diff = max_row - len(row)
		if diff > 0:
			m.append(row+[placeholder]*diff)
		else:
			m.append(row)
	return m

# ------------------------- test -------------------------

t1 = [[1],[2,2],[3,3,3]]
t2 = [['a','b','c'],['a','b','c','d','e','f'],['a','b','c','d','e','f','g'],['a','b','c','d']]
t3 = [['apple','apricot','peach'],['banana','cherry','cantaloupe','grapefruit','honeydew'],['papaya','plum']]
t4 = [[1,2],[2,1]]

def br():
	print('\n')
def hr():
	print('\n------------------------------\n')

br()
for a in t1:
	print(str(a))
br()
for a in matrix_form(t1, 0): 
	print(str(a))
hr()

for b in t2:
	print(str(b))
br()
for b in matrix_form(t2, ' '):
	print(str(b))
hr()

for c in t3:
	print(str(c))
br()
for c in matrix_form(t3, 'fruit'):
	print(str(c))
hr()

for d in t4:
	print(str(d))
br()
for d in matrix_form(t4, 3): 
	print(str(d))
hr()

input()