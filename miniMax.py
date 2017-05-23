import itertools
ar = [3,9,17,81]
a = list(itertools.permutations(ar))

maximum = 10000
for i in a:
	temp = []
	for j in xrange(len(ar)-1):
		temp.append(i[j] ^ i[j+1])
	if max(temp) < maximum:
		print i, max(temp)
		maximum = max(temp)
	if max(temp) == maximum:
		print i, max(temp)
		