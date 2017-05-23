#!/bin/python
#https://www.hackerrank.com/contests/w27/challenges/tailor-shop/submissions/code/8200932
import sys
from math import ceil

n,p = raw_input().strip().split(' ')
n,p = [int(n),float(p)]
a = sorted(map(int,raw_input().strip().split(' ')))
# your code goes here
b = int(ceil(a[0]/p))
c = b
d = set([c])
#print 'a',c
for i in a[1::]:
    s = max(int(ceil(i/p)),c+1)
    while True:
        if s not in d:
            d.add(s)
            c = s
            break
        s += 1
    #print c
    b += c
print b