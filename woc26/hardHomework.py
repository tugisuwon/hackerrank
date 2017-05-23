#https://www.hackerrank.com/contests/w26/challenges/hard-homework
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
import math
i = (1,1,n-2)
s = sum(math.sin(j) for j in i)
q = i
x = [i]
#aa = set(i)
for j in xrange(2,n):
    i = (j,j,n-2*j)
    if i[-1] < 1:
        break
    s = max(s,sum(math.sin(j) for j in i))
#print q
#print aa
print '{0:.9f}'.format(s)