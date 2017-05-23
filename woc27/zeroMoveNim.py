#!/bin/python
#https://www.hackerrank.com/contests/w27/challenges/zero-move-nim
import sys


g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    p = map(int,raw_input().strip().split(' '))
    # your code goes here
    r = 0
    for i in p:
        if i%2:
            r ^= (i+1)
        else:
            r ^= (i-1)
    print 'W' if r else 'L'
