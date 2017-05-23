import math
for i in xrange(3,50):
	s = [1,i-1]
	m,p = 0,[]
	while s[0] <= s[1]:
		temp = math.sin(s[0]) + math.sin(s[1])
		if temp > m:
			m = temp
			p = s
		s = [s[0]+1,s[1]-1]
	print i,p