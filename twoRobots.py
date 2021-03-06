import math

def diff(p,c):
	if p == '' or c == '':
		return 0
	else:
		return math.fabs(p-c)
		
def nodeCal(p,c):
	#print p,c
	score = diff(p,c)
	return score
	
def twoRobots(path,n,c,p1,p2,score,best):
	if c == n-1:
		#print 'score', score
		c1,c2 = path[c][0], path[c][1]
		#print 'last point', c1,c2
		#print min(nodeCal(p1,c1)+score,nodeCal(p2,c1)+score)
		return min(nodeCal(p1,c1)+score,nodeCal(p2,c1)+score)
	c1,c2 = path[c][0], path[c][1]
	print 'c',c
	if score > best[-1]:
		print 'reject'
		return score
	
	left = twoRobots(path,n,c+1,c2,p2,nodeCal(p1,c1)+score,best)
	right = twoRobots(path,n,c+1,p1,c2,nodeCal(p2,c1)+score,best)
	
	print 'intermediate', left, right, best
	temp = min(left,right,best[-1])
	if temp < min(best):
		best.append(temp)
	print 'after', left, right, best
	return best[-1]

def distance(path,n):
	d2 = []
	for i in xrange(n):
		c1,c2 = path[i][0], path[i][1]	
		d2.append(diff(c1,c2))
	return sum(d2)
	
if __name__ == '__main__':
	t = int(raw_input())
	for ii in xrange(t):
		#print 't',ii
		m,n = map(int, raw_input().split())
		path = []
		for _ in xrange(n):
			x,y = map(int, raw_input().split())
			path.append((x,y))
		c1,c2 = path[0][0],path[0][1]
		p1,p2,c,score,best = c2,'',1,0,[10**6]
		if n > 1:
			print int(twoRobots(path,n,c,p1,p2,score,best) + distance(path,n))
		else:
			print int(distance(path,n))