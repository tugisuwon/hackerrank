#!/bin/python

import sys


n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
m = []
s = [1,0,1]
p = [0,0,1,1,1,0,1]
for i in xrange(1,n+1):
    m.append([])
    for j in xrange(1,n+1):
        t = (i*j)**2
        if t < 4:
            m[-1].append(s[t-1])
        else:
            m[-1].append(p[(t-4)%7])
    #print m[-1]
#print m
a = [0]
r = []
for i in m:
    r.append(i)
for _ in xrange(3):
    rr = []
    d = 0
    for i in xrange(n):
        rr.append([r[j][i] for j in xrange(n)][::-1])
        d += sum(m[i][j] != rr[-1][j] for j in xrange(n))
    r = rr
    a.append(d)
    #print rr,d
        
for a0 in xrange(q):
    angle = int(raw_input().strip())
    print a[(angle%360)/90]
    
