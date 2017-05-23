from itertools import permutations

st = 'cccceeee'
perms = [''.join(p) for p in permutations(st)]

minimum, st_ans = 10000,[]
for s in perms:
	#print s
	n = len(s)

	k = [0] * n
	for i in xrange(1,n):
		ss = s[0:i+1]
		#print ss
		m,mm = 1,0
		while True:
			#print ss[0:m], ss[-(m):], m
			if ss[0:m] == ss[-m:]:
				mm = m
			if m >= len(ss)/2:
				break
			m += 1
		k[i] = mm
	if sum(k) < minimum:
		minimum = sum(k)
		st_ans = [s]
	elif sum(k) == minimum:
		st_ans.append(s)

print minimum, st_ans[0]