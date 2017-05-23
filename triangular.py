n = 4
m = 2
if n == 2:
	t = range(1,11)
elif n == 3:
	t = [1,2,1] + range(4,11)
else:
	t = [1, 2, 1]
	for i in xrange(4,n+1):
		new = [1] + [t[i] + t[i+1] for i in xrange(len(t)-1)] 
		if len(new) < 10:
			new += [1]
		#print new
		t = new[0:11]
	if len(t) < 10:
		for j in xrange(len(t),11):
			t += [j]
if m == 1:
	if n % 2 == 0:
		output = 1
	else:
		output = 0
elif m == 2:
	if n % 2 == 0:
		output = t[m-1] - 1
		
if m == n:
	output = 0
print t
print output