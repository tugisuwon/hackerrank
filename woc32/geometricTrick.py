# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import random
#import time
def factors(x,n):
    xx = x**2
    output = []
    for i in xrange(1,x):
        if xx%i == 0:
            if max(i,xx/i) < n+1:
                output.append((i-1,xx/i-1))
    return output

def factors1(x,n):
	output = []
	for i in xrange(1,int(x**0.5)+1):
		if x%i == 0:
			if max(i,x/i):
				output.append(i)
				if i != x/i:
					output.append(x/i)
	xx = x**2
	result = []
	#print output
	output = sorted(output)
	pp = set()
	for i in xrange(len(output)):
		if output[i] == 1:
			pp.add(1)
		else:
			pp.add(output[i])
			#pp.add(xx/output[i])
			for j in xrange(i,len(output)):
				temp = output[i]*output[j]
				#print x,temp
				if temp < x:
					pp.add(temp)
				else:
					break
	#print pp
	#print sorted(pp)
	for i in sorted(pp):
		if i < xx/i:
			result.append((i-1,xx/i-1))
		else:
			break
	return result
	
def geometricTrick(s):
	#start = time.time()
	n = len(s)
	nn = n+1
	# Complete this function
	p = [True] * nn
	p[0] = p[1] = False
	for i in xrange(2, int(nn**0.5)+1):
		if p[i]:
			p[i*i:nn:i] = [False] * len(p[i*i:nn:i])
	#print p
	#print time.time() - start

	ans = 0
	#index = {i:[0]*(n+1) for i in 'ac'}
	for i in xrange(n):
		if s[i] == 'b':

			if p[i+1]:
				tt = (i+1)**2-1
				if tt < n:
					if s[0]+s[tt] in ['ac','ca']:
						ans += 1
			else:
				#check = factors(i+1,n)
				check1 = factors1(i+1,n)
				for j in check1:
					if j[1] < n:
						if s[j[0]]+s[j[1]] in ['ac','ca']:
							ans += 1
	#print time.time() - start
	return ans
    

n = int(raw_input())
s = raw_input()
#print n,s
result = geometricTrick(s)
print(result)