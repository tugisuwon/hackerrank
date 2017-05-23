#https://www.hackerrank.com/contests/w26/challenges/taste-of-win
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,raw_input().split())
M = 10**9+7
from itertools import product
from math import factorial
x = range(1,2**m)
a = 0
for i in product(x,repeat=n):
    #print i
    if len(set(i)) == len(i):
        if list(i) == sorted(i):
        #if True:
            #print i
            res = reduce(lambda x, y: x ^ y, i)
            if res:
                #print i
                a += factorial(n)
print a%M