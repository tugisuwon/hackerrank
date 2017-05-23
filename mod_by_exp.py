def mod_by_exp(b,e,m):
	r = 1
	while e > 0:
		if e&1:
			r = (r*b)%m
		b = (b**2)%m
		e >>= 1
		print r,b,e
	return r
	
print mod_by_exp(4,13,497)