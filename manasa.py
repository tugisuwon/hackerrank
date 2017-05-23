def manasa(n):
	if len(n) < 3:
		if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
			print 'YES'
		else:
			print 'NO'
	else:
		output = 'NO'
		for index1, i in enumerate(n): 
			#print index1, i
			#print [x for ii,x in enumerate(n) if ii != index1]
			for index2, j in [(x,y) for x,y in enumerate(n) if x != index1]:
				#print index1, index2
				#print [x for jj,x in enumerate(n) if jj != index1 and jj != index2]
				for k in [x for jj,x in enumerate(n) if jj != index1 and jj != index2]:
					temp = int(i+j+k)
					#print temp
					if temp % 8 == 0:
						output = 'YES'
						break
				if output == 'YES':
					break
			if output == 'YES':
				break
		print output
if __name__ == '__main__':
    t = 1
    for _ in xrange(t):
        manasa('75')