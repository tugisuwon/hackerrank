#!/bin/python
#https://www.hackerrank.com/contests/w30/challenges/poles/submissions/code/1300991420
import sys

n,k = map(int,raw_input().split())
h,w = [],[]
for _ in xrange(n):
    a,b = map(int,raw_input().split())
    h = [a] + h
    w = [b] + w
limit = 1
if n - k <= limit:
    from itertools import combinations as co

    m = 10**9
    for i in co(range(n-1),k-1):
        i += (n-1,)
        #print i
        temp = 0
        start = 0
        for j in i:
            temp += sum(w[l]*(h[l]-h[j]) for l in xrange(start,j))
            #print j,temp
            start = j+1
            if temp >= m:
                break
        #print i,temp
        m = min(m,temp)
    print m
else:
    m = [[0 for _ in xrange(n)] for _ in xrange(n)]
    for i in xrange(n-1):
        for j in xrange(i+1,n):
            m[i][j] = w[i]*(h[i]-h[j])
    t = []
    for i in xrange(n):
        t.append((sum(m[a][i] for a in xrange(n)),i))
    #print t
    for i in xrange(1,k):
        #print 'i',i
        temp = []
        oo = max(0,i-2)
        start = 0
        for j in xrange(oo+1):
            temp.append((10**9,[]))
        for j in xrange(oo,n-1):
            best = 10**9
            for l in xrange(start,j+1):
                #print i,j,l,start
                check = t[l]
                #print 'check', check
                if check[1] != [] and l < n:
                    #print j, check, l, [m[a][j+1] for a in xrange(check[1]+1,n)]
                    c = check[0] + sum(m[a][j+1] for a in xrange(check[1]+1,j+1))
                    if best > c:
                        best = c
                        order = j+1
                        start = l
                #print best, order
            #print 'j', j, check, l, best, order, start
            temp.append((best,order))
        #print temp
        t = temp
        #print temp
        #print start
    print t[n-1][0]
