# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import date
import numpy as np

def trend(day, price, n):
	change = []
	for i in xrange(n-1):
		if price[i] != 'missing' and price[i+1] != 'missing':
			diff = price[i+1] - price[i]
			if i == 0:
				previous = (diff > 0)
			else:
				current = (diff > 0)
				if diff != 0:
					if previous != current:
						change.append(i+1)
				previous = current
		else:
			previous = True
	return change

def fillMissing(day,price,n,change):
	missing = [x for x in xrange(n) if price[x] == 'missing']
	#print 'missing', missing
	output = []
	for m in missing:
		if m == 0 or m < change[0]:
			start = 1
			last = change[0]
		elif m == n:
			start = change[-1]
			last = n-1
		else:
			if m > max(change):
				last = m - 1
				start = max(change)
				if start == last:
					start -= 1
			else:
				last = [x for x in change if x > m][0]
				start = change[change.index(last)-1]
		X = [day[i] for i in xrange(start,last) if price[i] != 'missing']
		y = [price[i] for i in xrange(start,last) if price[i] != 'missing']
		
		x = []
		for i in X:
			x.append([i] + [1])
		#print m, start, last
		#print x
		#print y
		c = np.linalg.lstsq(np.array(x),np.array(y))[0]
		#print np.dot(np.array([day[m]] + [1]),c)
		#print '-----------'
		output.append(np.dot(np.array([day[m]] + [1]),c))
			
	print '\n'.join([str(x) for x in output])		
			
	
if __name__ == '__main__':
	'''
	with open('input.txt') as f:
		n = int(f.readline())
		day, price = [], []
		for i in xrange(n):
			temp = f.readline().split()
			current = map(int, temp[0].split('/'))
			if i == 0:
				day.append(0)
				previous = date(current[2],current[0],current[1])
			else:
				d0 = previous
				d1 = date(current[2],current[0],current[1])
				delta = d1 - d0
				day.append(delta.days)
			
			if 'Missing' not in temp[-1]:
				price.append(float(temp[-1]))
			else:
				price.append('missing')
	'''
	n = int(raw_input())
	day, price = [], []
	for i in xrange(n):
		temp = raw_input().split()
		current = map(int, temp[0].split('/'))
		if i == 0:
			day.append(0)
			previous = date(current[2],current[0],current[1])
		else:
			d0 = previous
			d1 = date(current[2],current[0],current[1])
			delta = d1 - d0
			day.append(delta.days)
		
		if 'Missing' not in temp[-1]:
			price.append(float(temp[-1]))
		else:
			price.append('missing')
			
	change = trend(day, price, n)
	#print change
	fillMissing(day,price,n,change)