import time

start = time.time()
def primes(n):
	i = 2
	notPrime = 0
	while i * i <= n:
		#print n,i, factors
		if n % i:
			i += 1
		else:
			n //= i
			notPrime = 1
			break
	if notPrime == 0:
		return True

#print largestPrimeFactor(101)
print [x for x in ([2] + range(3,1000000,2)) if primes(x)]
print time.time() -start

