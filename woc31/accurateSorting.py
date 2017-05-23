#!/bin/python
#https://www.hackerrank.com/contests/w31/challenges/accurate-sorting
import sys

q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    b = [x for x in a]
    # Write Your Code Here
    for i in xrange(n-1):
        if a[i] == a[i+1] + 1:
            t = a[i]
            a[i] = a[i+1]
            a[i+1] = t
    print ['No','Yes'][sorted(b) == a]

