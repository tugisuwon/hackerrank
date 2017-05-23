#!/bin/python

import sys

def maxSumIS(arr, n):
	msis = [x for x in arr]
	index = range(n)

	# Compute maximum sum values in bottom up manner
	for i in range(1, n):
		for j in range(i):
			if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
				msis[i] = msis[j] + arr[i]
				index[i] = j
	print msis
	m = [msis[0]]
	for i in msis[1:]:
		m.append(max(m[-1],i))

	return m,index

n = 3
a = [0,3,1,6,4,2]
print maxSumIS(a,6)
'''
# your code goes here
s = [0]
for i in a:
    s.append(s[-1]+i)
c = -10**9
for i in xrange(n):
	for j in xrange(i,n):
		c1 = s[j+1]-s[i+1-1]
		t = a[i:j+1]
		c2 = maxSumIS(t,len(t))
		print i,j,t,c1,c2
		c = max(c,c1-c2)
print c
'''