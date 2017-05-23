final = []
for n in xrange(2,18):
	for m in xrange(1,11):

		t = [1]*m
		t[0] = n-m+1

		#print t

		l = {2:[t]}
		for i in xrange(2,m+1):
			checkP = 1
			l[i+1] = []
			for t in l[i]:
				initial = [x for x in t]
				#print 'i',i, initial
				while True:
					j = i-2
					while True:
						for kk in xrange(j+1,i):
							#print i,j,kk
							#print j,kk, initial[j], initial[kk],initial
							if initial[j] > initial[kk] + 1:
								initial[j] -= 1
								initial[kk] += 1
								#print 'a', initial,t,i,j,kk
								if initial not in l[i+1]:
									#print initial,l
									l[i+1].append([x for x in initial])
						if j == 0:
							break
						else:
							j -= 1
					checkPoint = [initial[x] - initial[x+1] for x in xrange(i-1)]
					check = [x > 1 for x in checkPoint]
					if sum(check) == 0:
						break
		output = []
		for k,v in l.iteritems():
			for vv in v:
				vv = sorted(vv,reverse=True)
				if vv not in output:
					output.append(vv)
		#print output, len(output)
		from math import factorial
		total = 0
		base = factorial(m)
		for initial in output:
			rem = [x%2 for x in initial if x != 1]
        
			#print initial
			valid = 1
			ti = [x for x in initial if x != 1]
			#ti = sorted(ti)
			if len(ti) % 2 == 0:
				cnt = 0
				for ll in xrange(len(ti)/2):
					if ti[2*ll] == ti[2*ll+1]:
						cnt += 1
				if cnt == len(ti)/2:
					valid = 0
			if k == 2:
				if rem.count(0) % 2 == 0:
					valid = 0
			if valid == 1:
				ttt = list(set(initial))
				tt = 1
				for i in ttt:
					tt *= factorial(initial.count(i))
				total += base/tt
		final.append((n,m,total))
output = {}
for i in xrange(1,11):
	output[i] = []
for i in final:
	a,b,c = i[0],i[1],i[2]
	output[b].append(c)

for k,v in output.iteritems():
	print v
	