# Enter your code here. Read input from STDIN. Print output to STDOUT
def coolGuy(ar,n,M):
	temp = []
	ans = 0
	count = 0
	for a in xrange(n):
		for b in xrange(a,n):
			for c in xrange(b+1,n):
				for d in xrange(c,n):
					print a,b,c,d, min(ar[a:b+1]+ar[c:d+1])
					ans = (ans + min(ar[a:b+1]+ar[c:d+1])) % M 
					temp.append(min(ar[a:b+1]+ar[c:d+1]))
					count += 1
	print ans, count
	t = {}
	for i in temp:
		if i in t:
			t[i] += 1
		else:
			t[i] = 1
	print t

if __name__ == '__main__':
	#n = int(raw_input())
	#ar = map(int, raw_input().split())
	#ar = sorted(ar)
	n = 6
	ar = [4,5,4,1,2,3]
	M = 10**9+7
	if n > 1:
		coolGuy(ar,n,M)
	else:
		print ar[0]%M