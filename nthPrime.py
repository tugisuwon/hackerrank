def nthPrime(n,primeList):
    print primeList[n-1]
    
def primes(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
			n //= i
			factors.append(i)
    if factors == []:
        return True


if __name__ == '__main__':
    #t = int(raw_input())
	t = 1
	primeList = [x for x in range(2,110000) if primes(x)]
	for _ in range(t):
        #n = int(raw_input())
		n = 100
		nthPrime(n,primeList)
		
scan 'elog_pn4', {FILTER => "SingleColumnValueFilter('c15', 'ruleIdApplied', =, 'substring:3')"} 