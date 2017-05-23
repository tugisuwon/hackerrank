#!/bin/python
#https://www.hackerrank.com/contests/w30/challenges/melodious-password/submissions/code/1300918312
import sys


n = int(raw_input().strip())
v = 'aeiou'
c = 'bcdfghjklmnpqrstvwxz'

p = list(v) + list(c)
for i in xrange(n-1):
    t = []
    for j in p:
        if j[-1] in v:
            for k in c:
                t += [j+k]
        else:
            for k in v:
                t += [j+k]
    p = t
for i in p:
    print i