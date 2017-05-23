n = 6
p = 1
print p
for i in xrange(1,n):
	p *= (n-i)/float(i)
	print p