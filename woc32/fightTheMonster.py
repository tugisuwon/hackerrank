#!/bin/python

import sys,math

def getMaxMonsters(n, hit, t, h):
    # Complete this function
    h = sorted(h)
    k = 0
    ans = 0
    while t > 0 and k < n:
        t -= int(math.ceil(h[k] / hit))
        if t >= 0:
            ans += 1
        k += 1
    return ans

n, hit, t = raw_input().strip().split(' ')
n, hit, t = [int(n), float(hit), int(t)]
h = map(int, raw_input().strip().split(' '))
result = getMaxMonsters(n, hit, t, h)
print(result)
