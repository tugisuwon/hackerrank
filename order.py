from itertools import permutations
n = 11
k = 4
x = ''.join([str(x) for x in range(1,n)])

candidate = [''.join(p) for p in permutations(x)]
order = range(1,n)
for i in candidate:
	temp = [int(y) for y in i]
	#print temp, order
	check = [abs(a-b) for a,b in zip(order,temp)]
	#print check, check.count(k)
	if check.count(k) == n-1:
		print i
		