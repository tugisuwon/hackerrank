for n in xrange(2,50):
	tt = [0]*n
	tt[0] = 1
	tt[1] = 1
	l = [tt]
	t = [0]*n
	t[0] = 1
	t[1] = 1
	for j in xrange(10000):
		t = [t[x-1]^t[x] for x in xrange(n)]
		#for j in s:
		#t = [s[0].count(x)%2 for x in a]
		#print ''.join([str(x) for x in t])
		#print i,s
		#l.append(t)
		if j > 0 and t in l:
			print n,j, l.index(t)
			break
		l.append(t)