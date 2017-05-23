from itertools import product
def pythagorean(a,b,c,n):
    #print a,b,c,a+b+c==n
    if a<=b and b<=c and a+b+c==n:
        print 'found', a**2 + b**2 == c**2
        return a**2 + b**2 == c**2

candidate = [a*b*c for a,b,c in product(xrange(1,int(1000)), repeat=3) if pythagorean(a,b,c,20)]


1 2 3 3 3 4 4 5 5 5 5 6 7 7 8 9

11, 11, 12, 10, 

n=int(input())
weights=[int(x) for x in raw_input().split(' ')]
weights.sort()
ans=1
rec=0
for i in range(1,n):
if(weights[i] not in [weights[rec],weights[rec]+1,weights[rec]+2,weights[rec]+3,weights[rec]+4]):
    ans+=1;
    rec=i;
print ans