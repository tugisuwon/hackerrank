#!/bin/python
#https://www.hackerrank.com/contests/w29/challenges/megaprime-numbers/submissions/code/1300663511
import sys
import random
def fermat(n):
    o = n - 1
    t = 0
    while o % 2 == 0:
        o = o / 2
        t = t + 1 
    for time in xrange(3):
        while True:
            r = random.randint(2, n)-1
            if r != 0 and r != 1:
                break
        
        rp = pow(r, o, n)
        if (rp != 1) and (rp != n - 1):
            i = 1
            while (i <= t - 1) and (rp != n - 1):
                rp = pow(rp, 2, n)
                i += 1

            if (rp != (n - 1)):
                return False
    return True 

first,last = raw_input().strip().split(' ')
first,last = [long(first),long(last)]
# your code goes here

kk,ll = str(first),str(last)
k = len(kk)
t = str(first)[0]
p = [x for x in '2357' if int(x) >= int(t)]
l = len(ll)
from itertools import product
n = 0

if k == l:
    duplicate = ''
    for i in xrange(k):
        if kk[i] == ll[i]:
            duplicate += kk[i]
        else:
            break
    if duplicate == '':
        for ii in p:
            for j in product('2357', repeat=l-1):
                j = ii + ''.join(j)
                p = int(j)
                #print p
                if p >= first:
                    if p == 2 or p == 5:
                        n += 1
                    elif j[-1] != '2' and j[-1] != '5':
                        if p <= last:
                            if fermat(p):
                                #print 'p',p
                                n += 1
                        else:
                            break
    else:
        for j in product('2357', repeat=l-i):
            j = duplicate  + ''.join(j)
            p = int(j)
            #print p
            if p >= first:
                if p == 2 or p == 5:
                    n += 1
                elif j[-1] != '2' and j[-1] != '5':
                    if p <= last:
                        if fermat(p):
                            #print 'p',p
                            n += 1
                    else:
                        break
else:
    for i in xrange(k,l+1):
        if i == k:
            for ii in p:
                for j in product('2357', repeat=i-1):
                    j = ii+''.join(j)
                    p = int(j)
                    if p >= first:
                        if p == 2 or p == 5:
                            n += 1
                        elif j[-1] != '2' and j[-1] != '5':
                            if p <= last:
                                if fermat(p):
                                    #print 'p',p
                                    n += 1
                            else:
                                break
        else:
            for j in product('2357',repeat=i):
                #print j,''.join(j)
                p = int(''.join(j))
                if p >= first:
                    if p == 2 or p == 5:
                        n += 1
                    elif j[-1] != '2' and j[-1] != '5':
                        if p <= last:
                            if fermat(p):
                                #print 'p',p
                                n += 1
                        else:
                            break
print  n