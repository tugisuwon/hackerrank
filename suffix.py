#!/bin/python

import sys
def rotate(l, n):
    return ''.join(l[n:] + l[:n])
from itertools import permutations
q = 1
for a0 in xrange(q):
	s = 'aapqowwicnvvkgghjsqpqieekjdsfsfekjdsfjs'
	# your code goes here
	nn = len(s)
	mm = s
	original = ''.join(x for x in s)
	ss = sorted(s)
	st = {s:0}
	#print ss
	for i in xrange(nn):
		p = {}
		for j,v in st.items():
			print j,v
			tt = 0
			if j[i] != ss[i]:
				candidate = j
				pp = [x-i for x in xrange(i,len(j)) if j[x]==ss[i]]
				#print pp
				for t in pp:
					temp = ''.join(j[:i] + rotate(j[i:],t))
					#print t,temp
					if temp[i] == ss[i]:
						print temp,v,p
						if temp not in p:
							p[temp] = v+1
						else:
							p[temp] = min(p[temp],v+1)
						tt = 1
						print 'p',p
			if tt == 0:
				if j in p:
					p[j] = min(p[j],v)
				else:
					p[j] = v
		st = p
		print i,p
	ans = len(s)
	for i,v in st.items():
		if i < s:
			s = i
			ans = v
		elif i == s:
			ans = min(ans,v)
	print ans
                  
        
