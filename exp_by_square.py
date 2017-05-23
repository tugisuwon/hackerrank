def exp_by_square(x,n):
	if n == 0:
		return 1
	elif n == 1:
		return x
	elif n % 2:
		return x*exp_by_square(x*x,(n-1)/2)
	elif n % 2 == 0:
		return exp_by_square(x*x,n/2)

print exp_by_square(2,15)

