#!/bin/python

n,q = map(int,raw_input().split())
s = raw_input()
import os

def lcp(a,b):
    return os.path.commonprefix([a,b])

d = {}
for _ in xrange(q):
    l,r = map(int,raw_input().split())
    #print l,r
    t = s[l:r+1]
    p = sorted(t[i:] for i in xrange(len(t)))
    #print p
    if len(t) == 1:
        print 1
    else:
        if (l,r) in d:
            print d[(l,r)]
        else:
            a = len(p[0])
            for i in xrange(len(p)-1):
                b,c = p[i],p[i+1]
                #print b,c
                a += len(c) - len(lcp(b,c))
            print a
            d[(l,r)] = a
        
