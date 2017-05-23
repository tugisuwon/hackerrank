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
    t = 1
    primeList = [x for x in range(2,2000000) if primes(x)]