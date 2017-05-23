#!/bin/python
#https://www.hackerrank.com/contests/w28/challenges/value-of-friendship/submissions/code/1300087737
for _ in xrange(int(raw_input())):
    n,m = map(int,raw_input().strip().split())
    a = {}
    order = 0
    o = 0
    v = [-1]*(n+1)
    for a1 in xrange(m):
        x,y = map(int,raw_input().strip().split())
        # your code goes here
        if a1 == 0:
            a[order] = set([x,y])
            v[x] = order
            v[y] = order
            order += 1
        else:
            if v[x] == v[y] == -1:
                a[order] = set([x,y])
                v[x] = order
                v[y] = order
                order += 1
            elif v[x] != -1 and v[y] == -1:
                a[v[x]].add(y)
                v[y] = v[x]
            elif v[y] != -1 and v[x] == -1:
                a[v[y]].add(x)
                v[x] = v[y]
            elif v[x] == v[y]:
                o += 1
            else:
                if len(a[v[x]]) > len(a[v[y]]):
                    a[v[x]] = a[v[x]].union(a[v[y]])
                    temp = v[y]
                    for l in a[v[y]]:
                        v[l] = v[x]
                    del a[temp]
                else:
                    #print v[y], a[v[y]].union(a[v[x]])
                    a[v[y]] = a[v[y]].union(a[v[x]])
                    temp = v[x]
                    for l in a[v[x]]:
                        v[l] = v[y]
                    del a[temp]
        #print a,v
    p = 0
    last = 0
    for i in sorted(a, key=lambda k: len(a[k]), reverse=True):
        j = len(a[i])
        #print sum(x*(x+1) for x in xrange(1,j))
        p += last*(j-1) + sum(x*(x+1) for x in xrange(1,j))
        last += j*(j-1)
    #print p,o,last
    print p + last*o
