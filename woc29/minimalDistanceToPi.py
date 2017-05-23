#!/bin/python
#https://www.hackerrank.com/contests/w29/challenges/minimal-distance-to-pi/submissions/code/1300716722
import sys


a,b = raw_input().strip().split(' ')
a,b = [long(a),long(b)]
# your code goes here
from math import pi
d,e = 0,1
pa = [7, 106, 113, 33102, 33215, 66317, 99532, 265381, 364913, 1360120, 1725033, 25510582, 52746197, 78256779, 131002976, 340262731, 811528438, 1963319607, 4738167652, 6701487259, 567663097408, 1142027682075, 1709690779483, 2851718461558, 44485467702853]
check = [x for x in pa if a<=x<=b]
if check != []:
    for i in check:
        t = pi*i
        p = abs(int(round(t))-t)
        if p < e:
            e = p
            d = [int(round(t)),i]
elif a == b:
    t = pi*a
    d = [int(round(t)),a]
else:
    start = [x for x in pa if x <= b]
    s = [x for x in pa if x <= a][-1]
    o = [x for x in pa if x >= b]
    i = s
    t = pi*i
    p = abs(int(round(t))-t)
    if p < e and a <= i <= b:
        e = p
        d = [int(round(t)),i]
    for k in start[::-1]:
        while i+k <= b:
            i += k
            t = pi*i
            p = abs(int(round(t))-t)
            if p < e and a <= i <= b:
                e = p
                d = [int(round(t)),i]
                #print e,d
    i = s
    for k in start[::-1]:
        while True:
            i += k
            if i >= a:
                t = pi*i
                p = abs(int(round(t))-t)
                if p < e and a <= i <= b:
                    e = p
                    d = [int(round(t)),i]
                i -= k
                break
    if o != []:
        i = o[0]
        for k in start[::-1]:
            while True:
                i -= k
                if i <= b:
                    t = pi*i
                    p = abs(int(round(t))-t)
                    if p < e and a <= i <= b:
                        e = p
                        d = [int(round(t)),i]
                    i += k
                    break
        i = o[0]
        for k in start[::-1]:
            while i-k >= a:
                i -= k
                t = pi*i
                p = abs(int(round(t))-t)
                if p < e and a <= i <= b:
                    e = p
                    d = [int(round(t)),i]
                
print str(d[0])+'/'+str(d[1])
