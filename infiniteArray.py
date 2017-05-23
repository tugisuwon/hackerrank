def sequenceElement(a, n):
	c = [a]
	total = [a]
	for i in xrange(n-5):
		a = a[1:] + [sum(a)%10]
		total += [sum(a)%10]
		if a in c:
			print 'yes'
			break
		else:
			c.append(a)
	print a, len(total), c[-10:], c.index(a), total[len(total)-6:]
	print total[-20:]
	total = total[:-6]
	print total[-5:],n%len(total)
	print total[n%len(total):]
	print total[(n+1)%(len(total))]

sequenceElement([7, 5, 4, 4, 8],521687676)