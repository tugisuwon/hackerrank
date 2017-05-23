a,b,c,d = 3000,3000,3000,3000
answer = []
count = 0
for i in xrange(1,a+1):
	for j in xrange(i,b+1):
		for k in xrange(j,c+1):
			if i^j^k >= max(i,j,k):
				#print i,j,k,i^j^k
				answer.append((i,j,k,i^j^k))
print count
for i in answer:
	print i