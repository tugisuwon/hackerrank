#!/bin/python

import sys

class DisjointSet(dict):
    def add(self, item):
        self[item] = item
 
    def find(self, item):
        parent = self[item]
 
        while self[parent] != parent:
            parent = self[parent]
 
        self[item] = parent
        return parent
 
    def union(self, item1, item2):
        self[item2] = self[item1]

from operator import itemgetter
 
def kruskal( nodes, edges ):
    forest = DisjointSet()
    mst = []
    for n in nodes:
        forest.add( n )
 
    sz = len(nodes) - 1
 
    for e in sorted( edges, key=itemgetter( 2 ), reverse=True ):
        n1, n2, _, _, _ = e
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        if t1 != t2:
            mst.append(e)
            sz -= 1
            if sz == 0:
                return mst
         
            forest.union(t1, t2)
            
n,m = map(int,raw_input().split())
e = {i:[] for i in xrange(n)}
f = {}
ff = {}
for _ in xrange(m):
    a,b,c,d = map(int,raw_input().split())
    e[a] += [b]
    e[b] += [a]
    cc = (min(a,b),max(a,b))
    if cc in f:
        #print f,f[cc],c,d
        dd = f[cc]
        if c/float(d) > dd[0]/float(dd[1]):
            f[cc] = (c,d)
            ff[cc] = (c,d,c/float(d))
        elif c/float(d) == dd[0]/float(dd[1]):
            if c < dd[0]:
                f[cc] = (c,d)
                ff[cc] = (c,d,c/float(d))
    else:
        f[cc] = (c,d)
        ff[cc] = (c,d,c/float(d))
#print ff
a = [str(x) for x in xrange(n)]
b = [(str(x[0]),str(x[1]),y[2],y[0],y[1]) for x,y in ff.items()]

e = {}
for i in b:
    if i[2] in e:
        e[i[2]].append(i)
    else:
        e[i[2]] = [i]
b = []
import operator
for i in sorted(e.keys(), reverse=True):
    b += sorted(e[i], key=operator.itemgetter(3))
#print b

c = kruskal(a,b)
#print a,b,c
answer = [0,0]
for i in c:
    answer[0] += i[3]
    answer[1] += i[4]
from fractions import gcd
g = gcd(answer[0],answer[1])
print str(answer[0]/g)+'/'+str(answer[1]/g)
