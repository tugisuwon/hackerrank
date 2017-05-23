n,q = 6,2
ar = [1,0,0,0,1,0]
query = [[0,5,1],[0,1,0]]
def bit(ar,i,j):
	tt = 0
	for x in xrange(i,j+1):
		for y in xrange(x,j+1):
			a = ar[x:y+1]
			t = a[0]
			for z in a[1::]:
				t ^= z
			tt += t
	return tt

d = []
for i in xrange(n):
	d.append([])
	for z in xrange(i):
		d[-1].append(0)
	dd = ar[i]
	for j in xrange(i,n):
		d[-1].append(bit(ar,i,j))
for i in d:
	print i
'''
for iii in xrange(q):
	i,j,k=query[iii]
	base = bit(ar,i,j)
	print ar[i:j+1], base
	if k > 0:
		for ii in xrange(len(ar)):
			temp = [xx for xx in ar]
			temp[ii] = (temp[ii] + 1)%2
			print temp[i:j+1],bit(temp,i,j)
			base = max(base,bit(temp,i,j))
	print base
'''