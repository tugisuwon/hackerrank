#!/bin/python
#https://www.hackerrank.com/contests/w30/challenges/substring-queries/submissions/code/1301012058
import sys
import re

def lcs(x,y):
    m,n = len(x),len(y)
    
    l = [0 for _ in xrange(n+2)]
    r = 0
    for i in xrange(m+1):
        ll = [0 for _ in xrange(n+2)]
        for j in xrange(n+1):
            if i == 0 or j == 0:
                ll[j] = 0
            elif x[i-1] == y[j-1]:
                ll[j] = l[j-1] + 1
                r = max(r,ll[j])
            else:
                ll[j] = 0
        l = ll
    return r

def lcs_re(s1,s2):
    output = 0
    i = 0
    for x in s1:
        if re.search(x,s2):
            s = x
            while re.search(s,s2):
                if len(s) > output:
                    output = len(s)
                if i+len(s) == len(s1):
                    break
                s = s1[i:i+len(s)+1]
        i += 1
    return output
                    
n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
s = []
ss = []
s_i = 0
for s_i in xrange(n):
    s_t = str(raw_input().strip())
    s.append(s_t)
    ss.append(set(s_t))
d = {}
for a0 in xrange(q):
    x,y = raw_input().strip().split(' ')
    x,y = [int(x),int(y)]
    # your code goes here
    a = (min(x,y),max(x,y))
    if a not in d:
        check = ss[x].intersection(ss[y])
        if check:
            if len(check) == 1:
                l = list(check)[0]
                p = 1
                for j in xrange(2,min(s[x].count(l),s[y].count(l))+1):
                    if not l*j in s[x] or not l*j in s[y]:
                        break
                    else:
                        p += 1
            else:
                p = lcs_re(s[x],s[y])
        else:
            p = 0
        d[a] = p
    else:
        p = d[a]
    print p