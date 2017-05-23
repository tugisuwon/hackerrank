h = [1,2,3]
a = [1,0,1]
for i in xrange(10000):
	h.append(h[-3]+h[-2]*2+h[-1]*3)
	a.append(h[-1]%2)
p = [0,0,1,1,1,0,1]

for n in xrange(5001,5050):
	print a[n],p[(n-3)%7]