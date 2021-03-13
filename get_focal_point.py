# params: (pts) a list of points
def get_focal_point(pts):
	ptlen = len(pts[0])
	r = [0]*ptlen
	for a in range(0,ptlen):
		for pt in pts:
			r[a] += pt[a]
		r[a] /= len(pts)
	return r

# ------------------------- test -------------------------

a = [
	[[1,2],[2,4]],
	[[1,2,3],[2,4,6]],
	[[1,5],[-2,3],[2,4],[0,1],[-3,-2]],
	[[20,54,59],[76,-39,41],[-60,32,-80],[10,87,-34],[51,-25,19]],
	[[-20,-30],[20,30]],
	]
for i in a:
	print("\n-----------------\n\n" + str(i) + "\n" + str(get_focal_point(i)))
input()