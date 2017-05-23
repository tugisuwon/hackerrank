def sol():
    N, A, B = 9,4,5
    S = 'aabaacaba'
    res = [0]*N
    res[0] = A
    maxl = 0
    for i in range(1,N):
		minv = res[i-1] + A
		cp, idx, newl = False, i, 0
		for k in range(maxl,-1,-1):
			print S[i-k:i+1], S[0:i-k]
			if S[i-k:i+1] in S[0:i-k]:
				cp, idx, newl = True, i-k, k+1
				break
		if cp: minv = min(minv, res[idx-1]+B)
		print minv, res[idx-1] + B
		print newl, idx
		maxl = newl
		res[i] = minv
		print i, res
    print res[-1]
T = 1
for x in range(T):
    sol()