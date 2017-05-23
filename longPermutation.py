ar = [2,1]
start = range(1,len(ar)+1)
n = len(ar)+1
m = 10
for i in xrange(m):
	new = [start[i-1] for i in ar] + [n]
	#print new
	start = new[1::]
	n += 1
print new[0]
