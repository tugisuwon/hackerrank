#!/bin/python
#https://www.hackerrank.com/contests/w31/challenges/zero-one-game/submissions/code/1301302049
import sys


g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    s = raw_input().strip().replace(' ','')
    # If Alice wins, print 'Alice' on a new line; otherwise, print 'Bob'
    ss = s[0]
    a = 0
    for i in xrange(1,len(s)-1):
        if s[i-1] == s[i+1] == '0':
            if s[i] == '1':
                a += 1
            else:
                ss += s[i]
        else:
            ss += s[i]
    ss += s[-1]
    #print s,ss,a
    for i in xrange(1,len(ss)-1):
        if ss[i-1] == ss[i+1] == '0':
            a += 1
    #print a
    print 'Alice' if a%2 else 'Bob'
