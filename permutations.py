#!/bin/python
# 12 27 58
import sys

fid = open('perm_data.txt')
d = []
M = 10**9+7
for i in xrange(1,17):
	t = [0]*i
	for j in xrange(int(round(i/2.))):
		temp = fid.readline().replace('\r\n','').replace('\n','').split(' ')
		t[j] = int(temp[1])%M
	d.append(t)
	print i,d
print d,len(d)