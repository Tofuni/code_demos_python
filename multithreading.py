import threading

def cube_numbers(ls):
	for a in ls:
		print(str(a) + "^3 = " + str(a**3))

def partition_list(ls=[], s=1):
	r, i, n, z = [], 0, len(ls)//s, len(ls)%s
	for a in range(0,s):
		r.append(ls[i:i+n])
		i+=n
		if z != 0:
			r[a].append(ls[i])
			z, i = z-1, i+1
	return r
	
pl = partition_list(ls=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
	31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,
	63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,
	95,96,97,98,99,100], s=10) # returns 10 partitions of the 100 element list

for p in pl: # start a thread for each partition to process
	a = threading.Thread(target=cube_numbers, args=(p,))
	a.start()
	print(a)
input()