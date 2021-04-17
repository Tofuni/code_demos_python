# params: (x) an integer number
def get_factors(x):
    i=1
    r=[]
    while (i <= x//i):
        if (x%i == 0):
            r.append(i)
            (i != x//i) and r.append(x//i)
        i+=1
    return r

# ------------------------- test -------------------------

a = [100, 36, 17, 826, 20, 3582, 1380648, 0, 1, 64, 148032]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\nfactors: " + str(get_factors(i)))
input()