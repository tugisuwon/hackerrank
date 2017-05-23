import time

start=time.time()
history = [0]*5*10**6
for j in xrange(2,4*10**5):
	current = str(j)
	counter = 1
	step = [j]
	if history[j] != 0:
		#print history[j],j
		counter = history[j]
	else:
		while j != 1:
			if j < 5*10**6:
				if history[j] != 0:
					counter += history[j]-1
					break
				elif j % 2 == 0:
					j = j / 2
				else:
					j = 3*j + 1
			elif j % 2 == 0:
				j = j / 2
			else:
				j = 3*j + 1

			step.append(j)
			counter += 1
	for index, l in enumerate(step):
		if l < 5*10**6:
			if history[l] == 0:
				history[l] = counter - index
	#print j, counter
#print history
print time.time() - start
tt = [5*10**6,100000,200000,300000,400000,500000,600000,7000000,8000000,9000000]
for i in xrange(10):
	t = tt[i]
	a = history[0:t+1]
	temp = max(a)
	candidate = len(a)-a[::-1].index(temp)-1
	print candidate
print time.time() - start
