import time
import random
start = time.time()
o = open('test','wb')
o.write(str(10**4)+'\r\n')
for _ in xrange(10**5):
	x = random.randint(10**8,10**10)
	o.write(str(x)+'\r\n')
	a = bin(x)[2:][::-1]
	#print sum(2**k for k in xrange(len(a)) if a[k] == '0')
print time.time() - start

	