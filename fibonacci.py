def pow_mod(x, y, z):
    number=[[1,1],[1,0]]
    while y:
		if y & 1:
			number = matmult(number,x,z)
		#print y
		y >>= 1
		#print 'after', y
		x = matmult(x,x,z)
    return number

def matmult(a,b,m):
	#print a,b,m
	zip_b = zip(*b)
	#print zip_b
	return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))%m for col_b in zip_b] for row_a in a]


mod = 10**9 + 7
#t=input()
a = [[1,1],[1,0]]
for i in range(1):
    A,B,N = 1,1,100
    t = pow_mod(a,N-1,mod)
    print (t[1][0]*B + t[1][1]*A)%mod