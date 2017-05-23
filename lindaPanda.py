def sieveOfEratosthenes(limit):
	primes = [2]
	a = [False] * 2 + [True] + [True, False] * (limit/2)
	for i in xrange(3, limit+1):
		if a[i]:
			primes.append(i)
			for n in xrange(2*i, limit+1, i):
				a[n] = False
	return primes
necessary_primes = sieveOfEratosthenes(10**6)

def phi(n):
	if n in necessary_primes:
		output = n - 1
	elif n == 1:
		output = 1
	else:
		output = n
		for i in necessary_primes:
			if n%i == 0:
				output *= (1 - 1./i)
				while n%i == 0:
					n /= i
			if n == 1:
				break
	return int(output)
	
T = 1
for i in xrange(T):
    A, B, X = 3,4,2
    PHI = phi(X)
    A = A % X
    B = B % PHI
    if(B<0):
        B+= PHI
    print pow(A,B,X)