from itertools import product
import time

start = time.time()
def pythagorean(a,b,c,n):
    #print a,b,c
    return a**2 + b**2 == c**2

def special(n):
    candidate = []
    for i in xrange(n/5,n/2+1):
        for j in xrange(i+1,n/2+1):
            k = n - i - j
            if pythagorean(i,j,k,n):
                #print i,j,k
                candidate.append(i*j*k)
            if i + j >= n:
                break
    #print candidate
    if candidate != []:
        return max(candidate)
    else:
        return -1

print special(3000)
print time.time() - start