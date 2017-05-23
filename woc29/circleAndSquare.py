#!/bin/python
#https://www.hackerrank.com/contests/w29/challenges/a-circle-and-a-square/submissions/code/1300638038
import sys


w,h = raw_input().strip().split(' ')
w,h = [int(w),int(h)]
cx,cy,r = raw_input().strip().split(' ')
cx,cy,r = [int(cx),int(cy),int(r)]
x1,y1,x3,y3 = raw_input().strip().split(' ')
x1,y1,x3,y3 = [int(x1),int(y1),int(x3),int(y3)]
# your code goes here

xc,yc = (x1+x3)/2.,(y1+y3)/2.
xd,yd = (x1-x3)/2.,(y1-y3)/2.
x2,y2 = xc - yd, yc + xd
x4,y4 = xc + yd, yc - xd

output = []
for i in xrange(h):
    output.append(['.']*w)
    for j in xrange(w):
        if (cx-j)**2+(cy-i)**2 <= r**2:
            output[-1][j] = '#'
        else:
            ab=(x1-x2,y1-y2)
            bc=(x4-x1,y4-y1)
            ab_dot = ab[0]**2+ab[1]**2
            bc_dot = bc[0]**2+bc[1]**2
            am=(j-x2,i-y2)
            bm=(j-x1,i-y1)
            ab_am = ab[0]*am[0] + ab[1]*am[1]
            bc_bm = bc[0]*bm[0] + bc[1]*bm[1]
            if 0 <= ab_am <= ab_dot and 0 <= bc_bm <= bc_dot:
                output[-1][j] = '#'

for i in output:
    print ''.join(i)