#!/bin/python
#https://www.hackerrank.com/contests/w26/challenges/best-divisor
import sys
def sumDigit(x):
    return sum(int(y) for y in str(x))

n = int(raw_input().strip())
a,b = 1,1
for i in xrange(1,int(round(n**0.5))+1):
    if n%i==0:
        #print i,n/i
        t = sumDigit(i)
        if t > a:
            a = t
            b = i
        elif t == a:
            if i < b:
                b = i
        s = sumDigit(n/i)
        if s > a:
            a = s
            b = n/i
        elif s == a:
            if n/i < b:
                b = n/i
print b
