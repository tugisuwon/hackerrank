import math
mod = 10**9+7
""" tan(x) = p/q
Recurrence relations used:
	tan(nx) = (tan((n-1)x)+tan(x))/(1-tan(x)*tan((n-1)*x))
	tan(a+b) = tan(a)+tan(b)/(1-tan(a)*tan(b))
"""
def find_ans(n,p,q):
	print n,p,q
	if n==1 :
		return (p,q)
	if n==0:
		return (0,1)
	x = find_ans(n/2,p,q)
	print x
	(a,b) = (x[0],x[1])
	#print(a,b)
	if n%2 ==0 :
		return ((a*b+b*a)%mod,((b*b-a*a)%mod+mod)%mod)
	(a1,b1) = ((a*q+b*p)%mod,((b*q-a*p)%mod+mod)%mod)
	return ((a*b1+b*a1)%mod,((b*b1-a*a1)%mod+mod)%mod)			
def ans(a,b):
	return (a*pow(b,mod-2,mod))%mod
for t in range(0,1):
	p,q,n = 5,6,7
	a,b = find_ans(n,p,q)
	#print(a,b)
	print(ans(a,b))