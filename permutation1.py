

def permutation(n,k):
	maxDiff = n/2
	if n % 2 == 0:
		if k > 2:
			print -1
		else:
			temp = []
			if k == 1:
				for i in xrange(n/2):
					temp += [n/2-i,n/2+maxDiff-i]
			else:
				for i in xrange(1,n/2+1):
					temp += [n/2+i,i]
			print ' '.join([str(x) for x in temp])
	elif n == 1:
		if k > 1:
			print -1
		else:
			print 1
	else:
		output, count = [], 0
		for i in xrange(1,n+1):
			candidate = [[i]]
			c = 1
			while True:
				#print c,candidate
				nextCandidate = []
				for temp in candidate:
					#print temp, temp[-1]
					last = temp[-1]
					next = range(1,last-maxDiff+1) + range(last+maxDiff,n+1)
					next = [xx for xx in next if xx not in temp]
					for item in next:
						nextCandidate.append(temp+[item])
				candidate = nextCandidate
				#print 'a',candidate
				c += 1
				if nextCandidate == []:
					break
				if c == n:
					count += len(candidate)
					break
			if count >= k:
				#print k - count + len(candidate),k,count
				print ' '.join([str(x) for x in candidate[k - count + len(candidate) - 1]])
				break
			#print i, count, k
			#a =raw_input('a')
		if k > count:
			print -1
permutation(1,2)						