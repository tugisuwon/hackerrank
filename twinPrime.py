# Enter your code here. Read input from STDIN. Print output to STDOUT
import random
def p(n):
    if n > 1:
        for t in xrange(3):
            r = random.randint(2, n)-1
            if ( pow(r, n-1, n) != 1 ):
                return False
        return True
    else:
        return False  
    
def pp(i):
    for j in xrange(3,int(round(i**0.5))+1,2):
        if i%j == 0:
            return False
    return True
n,m = 20000000,21000000
x = 100000

if n % 2 == 0:
    n += 1
a,aa = 0,0
while n < m:
    if pp(n) and pp(n+2):
            a += 1
    if p(n) and p(n+2):
            aa += 1
    n += 2
print a,aa
