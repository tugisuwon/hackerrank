#!/bin/python

import sys
from math import pi

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
r = raw_input().strip().split(' ')
# Write Your Code Here
r = {','.join(sorted(r)):1}
for _ in xrange(k):
    t = {}
    for i,j in r.items():
        i = i.split(',')
        for k1 in xrange(len(i)):
            for k2 in xrange(k1+1,len(i)):
                #print i[:k1], i[k1+1:k2], i[k2+1:] 
                temp = ','.join(sorted(i[:k1] + i[k1+1:k2] + i[k2+1:] + [str(int(i[k1]) + int(i[k2]))]))
                if temp not in t:
                    t[temp] = j
                else:
                    t[temp] += j
    r = t
output = 0
t = 0
#print r
for i,j in r.items():
    output += j*pi*sum(int(x)**2 for x in i.split(','))
    t += j
print output/t