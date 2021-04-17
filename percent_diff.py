# params: (i) integer, (j) integer
def percent_diff(i,j):
    return (j-i)/i*100

# ------------------------- test -------------------------

a = [
    [1,2],
    [5,35],
    [10,5],
    [500,300],
    [43.52,60.28],
    [740,397],
    [23.59, -16.11],
    [565.72,12290.23],
    [0.1,1]
]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n\npercent change: " + str(percent_diff(*i)))
input()