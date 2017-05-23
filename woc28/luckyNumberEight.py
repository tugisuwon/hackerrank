#!/bin/python
#https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight/submissions/code/1300061115
import sys


n = int(raw_input().strip())
a = raw_input().strip()
# your code goes here
M = 10**9+7
f = [0]*9
f[0] = 1
for i in xrange(n):
    ff = [0]*9
    for j in xrange(8):
        #print i+1,(j*10+int(a[i]))%8
        ff[(j*10+int(a[i]))%8] = (f[j]+ff[(j*10+int(a[i]))%8])%M
        ff[j] = (f[j]+ff[j])%M
    f = ff
print (ff[0]-1)%M