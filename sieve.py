def sieve(n):
	"Return all primes <= n."
	np1 = n + 1
	s = range(np1) # leave off `list()` in Python 2
	s[1] = 0
	sqrtn = int(round(n**0.5))
	for i in xrange(2, sqrtn + 1): # use `xrange()` in Python 2
		if s[i]:
			# next line:  use `xrange()` in Python 2
			s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
		print i,s
	return filter(None, s)

print sieve(100)