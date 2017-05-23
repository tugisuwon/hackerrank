#https://www.hackerrank.com/contests/w25/challenges/baby-step-giant-step
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
for _ in xrange(int(raw_input())):
    a,b,d = map(int,raw_input().split())
    n = 0
    if d > 2*b:
        n = int(math.ceil(d/float(b)))-2
        d -= b*n
    #print n,d
    #print n
    if d == a or d == b:
        print n+1
    elif d == a+b or d == 2*a or d == 2*b:
        print n+2
    elif d ==0:
        print n
    else:
        print n+2