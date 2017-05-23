#!/bin/python

import sys
import heapq as Q

def circularWalk(n, s, t, r_0, g, seed, p):
	# Complete this function
	if s == t:
		return 0
	cycle = [r_0]
	#print 'h'
	while True:
		new = (cycle[-1] * g + seed) % p
		if new in cycle:
			ss = cycle.index(new)
			break
		cycle.append(new)
	pp = len(cycle)
	if max(set(cycle)) == 1:
		return min((t-s)%n,(s-t)%n)
	cycle_ = cycle[:ss]
	cycle = cycle[ss:]
	pp -= ss
	start = [(0,s)]
	visited = [1]*(n+1)
	visited[s] = 0
	#print ss, cycle
	while start:
		next_ = []
		l_,u_,c1,c2 = 0,0,-1,-1
		for q in start:
			step, i = q
			#print i
			if i < ss:
				temp = cycle_[i]
			else:
				temp = cycle[(i-ss)%pp]
			lower, upper = (i-temp)%n, (i+temp)%n
			if lower > upper:
				if lower <= t or t <= upper:
					return step + 1
			else:
				if lower <= t <= upper:
					return step + 1

			for k in [x for x in xrange(-temp, temp+1) if visited[(i+x)%n]]:
				tt = (i + k)%n
				visited[tt] = 0
				if tt < ss:
					temp_ = cycle_[tt]
				else:
					temp_ = cycle[(tt-ss)%pp]
				if k-temp_ < l_:
					l_ = k-temp_
					c1 = tt
				if k+temp_ > u_:
					u_ = k+temp_
					c2 = tt
			#print l_,u_,c1,c2,k,temp_
		#print l_,u_,c1,c2,i,tt
		if c1 != -1:
			next_.append((step+1,c1))
		if c1 != c2 and c2 != -1:
			next_.append((step+1,c2))
		start = next_
	return -1
                
    

n, s, t = raw_input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
