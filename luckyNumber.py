import time

s = time.time()

n = 2*10**5
a = ''.join(str(x%10) for x in xrange(n))

M = 10**9+7
f = [0]*9
f[0] = 1
for i in xrange(n):
    ff = [0]*9
    for j in xrange(8):
        #print i+1,(j*10+int(a[i]))%8
        ff[(j*10+int(a[i]))%8] = (f[j]+ff[(j*10+int(a[i]))%8])%M
        ff[j] = (f[j]+ff[j])%M
    f = ff
print (ff[0]-1)%M
print time.time() - s