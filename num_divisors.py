def num_divisors(n):
	if n % 2 == 0: 
		n = n/2
	divisors = 1
	count = 0
	while n % 2 == 0:
		count += 1
		n = n/2
	#print count, n, divisors
	divisors = divisors * (count + 1)
	#print divisors
	p = 3
	while n != 1:
		count = 0
		while n % p == 0:
			count += 1
			n = n/p
		divisors = divisors * (count + 1)
		p += 2
	return divisors


print num_divisors(8)
print num_divisors(9)
print num_divisors(10)
print num_divisors(15)
print num_divisors(21)
print num_divisors(72)

[1, 1, 1] 1 [1, 1, 1]
[1, 1, 0] 0 [1, 1, 0]
[1, 0, 0] 0 [1, 0, 0]
[0, 0, 0] 0 [0, 0, 0]
[0, 1, 0] 1 [0, 0, 2]
[1, 0, 0] 1 [0, 2, 4]
[0, 0, 0] 0 [2, 4, 4]
[0, 0, 0] 0 [4, 4, 0]
[1, 1, 1] 0 [0, 0, 0]
[1, 1, 0] 2 [0, 0, 2]
[1, 0, 0] 4 [0, 2, 0]
[0, 0, 0] 4 [2, 0, 0]
[0, 0, 2] 0 [0, 0, 1]
[0, 2, 4] 0 [0, 1, 2]
[2, 4, 4] 2 [1, 2, 4]
[4, 4, 0] 0 [2, 4, 0]