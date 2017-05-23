#https://www.hackerrank.com/contests/w25/challenges/append-and-delete
#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

n = 0
while True:
    if s[n] == t[n]:
        n += 1
    else:
        break
    if n == min(len(s),len(t)):
        break
p = len(s)-n
q = len(t)-n
if k < p+q:
    print 'No'
elif k == p+q:
    print 'Yes'
else:
    if k > len(s)+len(t):
        print 'Yes'
    else:
        w = p+q
        if (k-w)%2 == 0:
            print 'Yes'
        else:
            print 'No'