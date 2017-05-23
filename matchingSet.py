# Enter your code here. Read input from STDIN. Print output to STDOUT
import random
import time
start = time.time()
n = 1
#a = [random.randrange(-10**9,10**9,1) for _ in range (n)]
#b = [random.randrange(-10**9,10**9,1) for _ in range (n)]
#a = [1]
#b = [2]
a,b = sorted(a),sorted(b)
aa,bb = [],[]
i,j = 0,0
while i < n or j < n:
    #print i,j,a[i],b[j]
    if j == n:
        aa.append(a[i])
        i += 1
    elif i == n:
        bb.append(b[j])
        j += 1
    elif a[i] == b[j]:
        i += 1
        j += 1
    elif a[i] > b[j] and j < n-1:
        bb.append(b[j])
        j += 1
    elif a[i] < b[j] and i < n-1:
        aa.append(a[i])
        i += 1
    else:
        aa.append(a[i])
        bb.append(b[j])
        i += 1
        j += 1
print aa,bb
if aa != []:
    x = [aa[i]-bb[i] for i in xrange(len(aa))]
    o = 0
    #print x
    if sum(x) != 0:
        print -1
    else:
        for i in x:
            if i > 0:
                o += i
        print o
else:
    print 0
print time.time()-start