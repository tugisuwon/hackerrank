import random
import time

def fermat(n):
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

start = time.time()	
n = "0xcd62eae0d72bc21"
x = int(n,16)
print x
# Start point assuming p and q size are similar
k = int(round((x**0.5)))
print k
if k%2==0:
	k += 1
p = 1
step = 0
while p:
	if fermat(k):
		if x%k == 0:
			print k,x/k
			p = 0
			break
	step += 1
	if step % 100000 == 0:
		print step,k
	k -= 2
print time.time() - start