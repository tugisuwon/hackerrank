#https://www.hackerrank.com/contests/w26/challenges/pairs-again
# Enter your code here. Read input from STDIN. Print output to STDOUT
def divisors(x):
    t = set([x])
    for i in xrange(2,int(round(x**0.5))+1):
        if x%i == 0:
            t.add(i)
            t.add(x/i)
    return t

def divisors1(x,m):
    t = set([x])
    for i in xrange(2,int(round(x**0.5))+1):
        if x%i == 0:
            if i > m:
                t.add(i)
            if x/i > m:
                t.add(x/i)
    return t

n = int(raw_input())
d = {}
a = set()
for i in xrange(2,n):
    a.add(i)
    d[i] = set()
d[1] = a
d[n] = set()
o = {}
for i in xrange(n,1,-1):
    if i in o:
        t = o[i]
    else:
        t = divisors(i)
        o[i] = t
    #print 'aaaa',i,t
    #a = set()
    if t == []:
        p = n-i
        #tt = divisors1(p,i)
        for kk in divisors1(p,i):
            a.add((i,kk))
    else:
        p = n-i
        if p in o:
            tt = o[p]
        else:
            tt = list(divisors(p))
            o[p] = tt
        for j in t:
            for kk in set([x for x in tt if x > j]):
                a.add((j,kk))

#print d
           
print len(a)