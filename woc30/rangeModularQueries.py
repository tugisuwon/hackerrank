#!/bin/python
#https://www.hackerrank.com/contests/w30/challenges/range-modular-queries/submissions/code/1300991725
import sys


n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
a = map(int, raw_input().strip().split(' '))
d = []
dd = set()
ddd = set()
qq = []
qqq = set()
for a0 in xrange(q):
    left,right,x,y = raw_input().strip().split(' ')
    left,right,x,y = [int(left),int(right),int(x),int(y)]
    # your code goes here
    if (x,y) in qqq:
        ddd.add((x,y))
    elif x in d:
        dd.add(x)
    qq.append((left,right,x,y))
    qqq.add((x,y))
    d.append(x)
aa = {}
for ii in dd:
    aa[ii] = [a[i]%ii for i in xrange(n)]
aaa = {}
for i in ddd:
    temp = [0]
    for j in xrange(n):
        temp += [temp[-1] + [0,1][a[j]%i[0]==i[1]]]
    aaa[i] = temp
#print aa
#print aaa
for i in qq:
    #print 'i',i
    left, right = i[0],i[1]
    if (i[2],i[3]) in aaa:
        p = aaa[(i[2],i[3])]
        #print p
        print p[right+1] - p[left]
    elif i[2] in aa:
        temp = aa[i[2]]
        print sum(1 if temp[ii] == i[3] else 0 for ii in xrange(left, right+1))
    else:
        print sum(1 if a[ii]%i[2] == i[3] else 0 for ii in xrange(left, right+1))
