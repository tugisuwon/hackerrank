#h = [50,15,10,5]
#w = [1,1,1,1]
h = [32,30,18,16,12,10]
w = [1,10,13,18,17,15]

from itertools import combinations

n,k = 6,3
m = [[0 for _ in xrange(n)] for _ in xrange(n)]
for i in xrange(n-1):
    for j in xrange(i+1,n):
        m[i][j] = w[i]*(h[i]-h[j])

for i in m:
	print i
	
output = []
for i in xrange(2,n+1):
	t = []
	for jj in xrange(1,k+1):
		m = 10**9
		best = ''
		for kk in combinations(range(i-1),jj-1):
			kk += (i-1,)
			temp = 0
			start = 0
			for j in kk:
				temp += sum(w[l]*(h[l]-h[j]) for l in xrange(start,j))
				#print j,temp
				start = j+1
				if temp >= m:
					break
			#print kk,temp
			if temp < m:
				m = temp
				best = kk
			#m = min(m,temp)
		#print i,jj,m,best
		t.append((m,best))
	output.append(t)

m = [[0 for _ in xrange(n)] for _ in xrange(n)]
for i in xrange(n-1):
    for j in xrange(i+1,n):
        m[i][j] = w[i]*(h[i]-h[j])	

t = []
t.append([(0,0) for _ in xrange(k)])
start = [0 for _ in xrange(k+1)]
for i in xrange(1,n):
	#print 'i',i
	temp = []
	temp.append((sum(m[a][i] for a in xrange(n)),i))
	for j in xrange(1,min(k,i)+1):
		best = 10**9
		order = []
		for l in xrange(start[j],i):
			#print i,j,l,start
			check = t[l][j-1]
			#print 'check', check
			if check[1] != []:
				#print check, i-1, [m[a][i] for a in xrange(check[1][-1]+1,n)]
				c = check[0] + sum(m[a][i] for a in xrange(check[1]+1,i+1))
				if best > c:
					best = c
					order = i
					start[j] = l
		check = temp[-1]
		#print order, best
		if check[1]:
			#print check, i-1, [m[a][i] for a in xrange(check[1][-1]+1,n)]
			c = check[0] + sum(m[a][i] for a in xrange(check[1]+1,i+1))
			if best > c:
				best = c
				order = i
				start[j] = i
		temp.append((best,order))
	for j in xrange(min(k,i)+1,n):
		temp.append((0,0))
	#print temp
	t.append(temp)
print 't', t
for i in output:
	print i