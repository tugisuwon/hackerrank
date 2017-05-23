import time

start = time.time()

a,b,c,d = 500,500,500,500
count = 0
'''
t1 = []
for i in xrange(1,a+1):
	for j in xrange(i,b+1):
		for k in xrange(j,c+1):
			n = 0
			for l in xrange(k,d+1):
				if i^j^k^l != 0:
					count += 1
					n += 1
			#print i,j,k,n
'''
print time.time() - start
start = time.time()
output = 0
for i in xrange(1,a+1):
	for j in xrange(i,b+1):
		for k in xrange(j,c+1):
			n = d+1-k
			if i == j:
				n -= 1
			t = i^j^k
			#print n,t,d
			if t > k and t <= d:
				n -= 1
			output += n
			#print i,j,k,n
print time.time() - start
start = time.time()
output = 0
for i in xrange(1,a+1):
	for j in xrange(i,b+1):
		n = (c+1-j) * (d+1)
			#print i,j,k,n
print output
print 'answer',count
print time.time() - start