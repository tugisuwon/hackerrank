# Enter your code here. Read input from STDIN. Print output to STDOUT
#n = int(raw_input())
import math
for n in xrange(3,100):
	i = (1,1,n-2)
	s = sum(math.sin(j) for j in i)
	q = [i]
	x = [i]
	#aa = set(i)
	while True:
		ne = set()
		for y in x:
			if y[2] > y[1] + 1:
				t = (y[0],y[1] + 1,y[2] - 1)
				temp = sum(math.sin(j) for j in t)
				
				if temp > s:
					s = temp
					q = [t]
				elif temp == s:
					q.append(t)
				ne.add(t)
				#aa.append(t)
			if y[1] > y[0] + 1:
				t = (y[0] + 1,y[1] - 1,y[2])
				temp = sum(math.sin(j) for j in t)
				
				if temp > s:
					s = temp
					q = [t]
				elif temp == s:
					q.append(t)
				
				ne.add(t)
				#aa.add(t)
		#print x,ne
		if len(ne)==0:
			break
		x = ne
	if n%3 == 0:
		s = max(s,3*math.sin(n/3.))
	#print q
	#print aa
	print n,q,'{0:.9f}'.format(s)