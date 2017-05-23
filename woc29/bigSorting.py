#!/bin/python
#https://www.hackerrank.com/contests/w29/challenges/big-sorting/submissions/code/1300620241
import sys
import operator

n = int(raw_input().strip())
a = {}
for i in xrange(n):
    t = str(raw_input().strip())
    u = len(t)
    if u not in a:
        a[u] = [t]
    else:
        a[u].append(t)
# your code goes here
o = []
a = sorted(a.items(), key=operator.itemgetter(0))
#print a
for i,j in a:
    for k in sorted(j):
        print k
