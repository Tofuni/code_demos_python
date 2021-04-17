# params: (ns) list of whole numbers
def weighted_percents(ns):
    s = 0
    r = []
    for n in ns:
        s+=n
    i = 100/s
    for n in ns:
        r.append(round(n*i, 3))
    return r

# ------------------------- test -------------------------

a = [
    [1,1],
    [1,1,2],
    [1,2,3,4],
    [100,200,300,400],
    [2,2,2,3,3,8],
    [12,54,29,76,62],
    [8,4,2,8,1,9,6,3,9,4,0,2],
    [348,765,105,397,382,871,507,109]
]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n" + str(weighted_percents(i)))
input()