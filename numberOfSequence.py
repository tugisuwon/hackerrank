# Enter your code here. Read input from STDIN. Print output to STDOUT
#n = 100000
#ar = [-1]*n
n = 12
ar = [0,1,2,-1,-1,5,6,-1,8,9,10,-1]
M = 10**9+7
import time
sss = time.time()

import math
def isPower (num, base):
    if base == 1 and num != 1: return False
    if base == 1 and num == 1: return True
    if base == 0 and num != 1: return False
    power = int (math.log (num, base) + 0.5)
    return base ** power == num
	
p = range(n+1)
p[1] = 0
for i in xrange(2,int(round((n+1)**0.5))+1):
    if p[i]:
        p[i*i:n+1:i] = [0]*len(xrange(i*i,n+1,i))
p = filter(None,p)

o = [1]*(n)
if ar[0] > 0:
    print 0
else:
	nonzeros = [x+1 for x in xrange(n) if ar[x] != -1]
	print 'a',nonzeros
	for i in p:
		c = [x for x in nonzeros if isPower(x,i)]
		if c == []:
			j = 1
			while i**j-1 <= n: 
				#print i**j-1,len(o)
				o[i**j-1] = i
				j += 1
		else:
			j = 1
			print c[-1]
			while i**j-1 <= c[-1]:
				o[i**j-1] = 1
				j += 1
			while i**j-1 < n:
				o[i**j-1] = i
				j += 1
		print i,o
	print time.time()-sss
	pp = reduce(lambda x, y: x*y%M, o)
	print pp%M