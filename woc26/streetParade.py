#https://www.hackerrank.com/contests/w26/challenges/street-parade-1
# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(raw_input())
a = map(int,raw_input().split())
m,h1,h2 = map(int,raw_input().split())

a = [a[0]-10**9] + a + [a[-1]+10**9]
if q == 1:
    print a[0]-h2
else:
    d = [a[i+1]-a[i] for i in xrange(q+1)]
    ans = a[1]-h2
    c,t,p = 0,0,0
    for i in xrange(len(d)):
        #print i,c,p
        if h1 <= d[i] <= h2 or i == len(d)-1:
            c += d[i]
            if t == 0:
                t = 1
                p = i-1
        else:
            c = 0
        if c == m:
            ans = a[p+1]
            break
        elif c > m:
            pp = m - (c - d[i])
            #print 'a',c,pp,p,d[p]
            h = -1
            if h1 <= pp <= h2:
                ans = a[p+1]
            elif pp >= h1 and h1<=d[p]:
                for k in xrange(h1,h2+1):
                    if (h1<=pp-k<=h2) and d[p] >= k:
                        h = k
                        break
            else:
                c -= d[p]
                p += 1
            if h != -1:
                #print 'b',p,h,a[p+1]
                ans = a[p+1] - h
                break
    #print d         
    print ans