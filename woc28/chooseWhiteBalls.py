#!/bin/python

import sys


n,k = map(int,raw_input().split())
b = raw_input().strip()
b = ''.join(['0','1'][x=='W'] for x in b)
# your code goes here

def verify(x):
    l = len(x)/2
    s = sum(int(x[k]) or int(x[-(k+1)]) for k in xrange(l))*2
    if len(x) % 2:
        s += 1*(int(x[l])==1)
    return s

e = 0
d = {b:1.0}
for kk in xrange(k):
    nn = {}
    if kk < k-1:
        #total = sum(a for q,a in d.items())
        p = 0
        for v,a in d.items():
            w = 0
            for i in xrange(len(v)/2):
                '''
                if v[i] == '1' and v[n-i-1] == '0':
                    t = ''.join([v[x] for x in xrange(n) if x != i])
                    w += 2
                elif v[i] == '0' and v[n-i-1] == '1':
                    t = ''.join([v[x] for x in xrange(n) if x != n-i-1])
                    w += 2
                '''
                if True:
                    t1 = ''.join([v[x] for x in xrange(n) if x != i])
                    t2 = ''.join([v[x] for x in xrange(n) if x != n-i-1])
                    s1,s2 = verify(t1),verify(t2)
                    ss1 = 1*(v[i]=='1')+ s1/float(n-1)
                    ss2 = 1*(v[n-i-1]=='1') + s2/float(n-1)
                    if ss1 > ss2:
                        t = t1
                        if v[i] == '1':
                            w += 2
                    elif ss2 > ss1:
                        t = t2
                        if v[n-i-1] == '1':
                            w += 2
                    else:
                        if t1 == t2 or t1 == t2[::-1]:
                            t = t2
                            if v[n-i-1] == '1':
                                w += 2
                        else:
                            ii = len(t1)
                            sss1 = abs(t1[:ii/2].count('1')-t1[:ii/2].count('0'))
                            sss2 = abs(t2[:ii/2].count('1')-t2[:ii/2].count('0'))
                            if sss1 > sss2:
                                t = t1
                                if v[i] == '1':
                                    w += 2
                            else:
                                t = t2
                                if v[n-i-1] == '1':
                                    w += 2
                if t in nn:
                    nn[t] += 1/float(n)*a*2
                else:
                    nn[t] = 1/float(n)*a*2
            if len(v) % 2:
                t = ''.join([v[x] for x in xrange(n) if x != len(v)/2])
                if v[len(v)/2] == '1':
                    w += 1
                if t in nn:
                    nn[t] += 1/float(n)*a
                else:
                    nn[t] = 1/float(n)*a
            p += w/float(len(v))*a
        #print 'k',kk,p
    else:
        p = 0
        for v,a in d.items():
            w = 0
            for i in xrange(len(v)/2):
                if v[i] == '1' or v[n-(i+1)] == '1':
                    w += 2
            #print v,w
            if len(v) % 2:
                if v[len(v)/2] == '1':
                    w += 1
            p += w/float(len(v))*a
    #print 'check',nn,p
    d = nn
    e += p
    n -= 1
print e
        
    
