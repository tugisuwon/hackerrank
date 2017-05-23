#n,m = map(int,raw_input().split())
M = 10**9+7
from itertools import product
from math import factorial
for n in xrange(7,8):
	for m in xrange(4,5):
		x = range(1,2**m)
		a = 0
		for i in product(x,repeat=n):
			#print i
			if len(set(i)) == len(i):
				if list(i) == sorted(i):
				#if True:
					#print i
					res = reduce(lambda x, y: x ^ y, i)
					if res:
						#print i
						a += factorial(n)
		print n,m,a%M,(a%M)/n,(a%M)%n