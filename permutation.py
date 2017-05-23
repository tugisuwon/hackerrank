from itertools import permutations
from math import fabs
x = '12345'
perms = [' '.join(p) for p in permutations(x)]
n = len(x)
output = 0
for items in perms:
	temp = map(int, items.split(' '))
	if min([fabs(temp[i+1] - temp[i]) for i in xrange(n-1)]) >= n/2:
		output += 1
		print items
print output