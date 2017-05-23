#https://www.hackerrank.com/contests/w26/challenges/twins
# Enter your code here. Read input from STDIN. Print output to STDOUT
import random
def p(n):
    o = n - 1
    t = 0
    while o % 2 == 0:
        o = o / 2
        t = t + 1 
    for time in xrange(3):
        while True:
            r = random.randint(2, n)-1
            if r != 0 and r != 1:
                break
        
        rp = pow(r, o, n)
        if (rp != 1) and (rp != n - 1):
            i = 1
            while (i <= t - 1) and (rp != n - 1):
                rp = pow(rp, 2, n)
                i += 1

            if (rp != (n - 1)):
                return False
    return True 
    
def pp(i):
    for j in xrange(3,int(round(i**0.5))+1,2):
        if i%j == 0:
            return False
    return True
n,m = map(int,raw_input().split())
x = 1

if n % 2 == 0:
    n += 1
a = 0
if n == 1:
    b = 0
else:
    b = p(n)
while n + 2 <= m:
    c = p(n+2)
    if b and c:
        a += 1
    b = c
    n += 2
print a
