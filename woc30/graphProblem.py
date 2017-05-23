#!/bin/python
#https://www.hackerrank.com/contests/w30/challenges/a-graph-problem/submissions/code/1300990991
import sys


n = int(raw_input().strip())
g = {}
for i in xrange(n):
    g_temp = map(int,raw_input().strip().split(' '))
    g[i] = [k for k in xrange(n) if g_temp[k] == 1]
# your code goes here
t = set()
for i in xrange(n):
    s = [[i]]
    ss = []
    for j in s:
        for k in g[j[-1]]:
            if k not in j:
                ss.append(j+[k])
    s = []
    for j in ss:
        for k in g[j[-1]]:
            if k not in j:
                s.append(j+[k])
    for j in s:
        if i in g[j[-1]]:
            t.add(tuple(sorted(j)))
t = list(t)
#print t
p, s = 0,''
visited = set()
for i in xrange(len(t)):
    if i not in visited:
        visited.add(i)
        start = set(t[i])
        current = 3
        ii = 1
        for j in xrange(i+1,len(t)):
            if j not in visited:
                if start.intersection(set(t[j])):
                    visited.add(j)
                    start = start.union(set(t[j]))
                    ii += 1
                    temp = ii/float(len(start))
                    if temp > p:
                        p = temp
                        s = list(start)
#print s
if p == 0:
    if t:
        print 3
        print ' '.join(str(x+1) for x in t[0])
    else:
        print n
        print ' '.join(str(x) for x in range(1,n+1))
else:
    print len(s)
    print ' '.join(str(x+1) for x in sorted(s))