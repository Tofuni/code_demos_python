# params: (data) an array of numbers, (x) number of items in each set
def sets_of_x(data, x):
    r = []
    i = 0
    for a in range(len(data)//x):
        r.append(data[i:i+x])
        i+=x
    (len(data[i:len(data)]) > 0) and r.append(data[i:len(data)])
    return r

# ------------------------- test -------------------------

a = [
    [[1,2,3,4,5,6,7,8,9,10,11], 2],
    [[1,2,3,4,5,6,7,8,9,10,11], 3],
    [[1,2,3,4,5,6,7,8,9,10,11], 4],
    [['a','b','c','d','e','f','g','h','i'], 3],
    [['a','b','c','d','e','f','g','h','i'], 4]
]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n" + str(sets_of_x(*i)))
input()