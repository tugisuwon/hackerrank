#!/bin/python

import sys

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
A = map(int, raw_input().strip().split(' '))
C = map(int, raw_input().strip().split(' '))
B = []
for _ in xrange(n):
    B.append(map(int,raw_input().strip().split(' ')))
# Write Your Code Here
#print B
count = [0] * m
possibilities = []
for i in xrange(n):
    for j in xrange(m):
        possibilities.append((i,j,B[i][j]))

p = sorted(possibilities, key=lambda tup:tup[2], reverse=True)
#print p
oo = 25
cases = [(0,[x for x in A],[x for x in count])]
while p:
    current = p.pop(0)
    nextCases = []
    minValue = 10**9
    for cc in cases:
        ans = cc[0]
        AA = [x for x in cc[1]]
        count_ = [x for x in cc[2]]
        if len(nextCases) > oo:
            nextCases = sorted(nextCases, key=lambda tup: tup[0], reverse=True)
            if nextCases[-1][0] < ans:
                nextCases = nextCases[:-1] 
                nextCases.append(tuple(x for x in cc))
        else:
            nextCases.append(tuple(x for x in cc))
        
        #print nextCases
        j = current[1]
        if AA[current[0]] > 0:
            c = count_[j] + 1
            ans += current[2]
            count_[j] += 1
            AA[current[0]] -= 1
            temp_ = (ans,AA,count_)
            if temp_ != cc:
                if len(nextCases) > oo:
                    nextCases = sorted(nextCases, key=lambda tup: tup[0], reverse=True)
                    if nextCases[-1][0] < ans:
                        nextCases = nextCases[:-1] 
                        nextCases.append(temp_)
                else:
                    nextCases.append(temp_)
                #nextCases.append(temp_)
    #print current, nextCases
    cases = nextCases
ans = 0
for i in cases:
    temp = i[0]
    for j in xrange(m):
        if i[2][j] > C[j]:
            temp -= (i[2][j] - C[j])**2
    ans = max(ans,temp)
print ans