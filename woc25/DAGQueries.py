#https://www.hackerrank.com/contests/w25/challenges/dag-queries

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m,q = map(int,raw_input().split())
d = {}
p = [0]*(n+1)
for _ in xrange(m):
    a,b = map(int,raw_input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]
f = {}
for _ in xrange(q):
    t = map(int,raw_input().split())
    if t[0] == 3:
        print p[t[1]]
    else:
        if t[1] in f:
            w = f[t[1]]
        else:
            a = [t[1]]
            w = set()
            w.add(t[1])
            while a != []:
                b = set()
                for i in a:
                    if i in d:
                        for j in d[i]:
                            w.add(j)
                            b.add(j)
                a = list(b)
            f[t[1]] = w
        #print w,t[2],'a'
        if t[0] == 1:
            for k in w:
                p[k] = t[2]
        else:
            for k in w:
                #print k,p[k],t[2]
                if p[k] > t[2]:
                    p[k] = t[2]