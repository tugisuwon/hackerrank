def coolGuy(ar,n,M):
	
	ans = 0
	count = 0
	n = n-1
	while len(ar) != 1:
		for b in xrange(n):
			for c in xrange(b+1,n):
				for d in xrange(c,n):
					print b,c,d
					#print min(ar[a:b+1] + ar[c:d+1])
					count += 1
					ans = (ans + min([ar[b]] + ar[c:d+1])) % M 
		ar = ar[1::]
		n -= 1
		print len(ar),'h'
	print ans, count

if __name__ == '__main__':
	#n = int(raw_input())
	#ar = map(int, raw_input().split())
	#ar = sorted(ar)
	n = 6
	ar = [3,2,1,4,5,6]
	M = 10**9+7
	if n > 1:
		coolGuy(ar,n,M)
	else:
		print ar[0]%M