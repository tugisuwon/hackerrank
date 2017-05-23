#https://www.youtube.com/watch?v=cETfFsSTGJI&spfreload=1

def minimumJump(ar):
	n = len(ar)
	numOfJumps = [0] * n
	index = [0] * n
	index[0] = -1
	i,j = 0,1
	while True:
		if j <= i + ar[i]:
			if numOfJumps[j] == 0:
				numOfJumps[j] = numOfJumps[i] + 1
				index[j] = i
			else:
				if numOfJumps[j] > numOfJumps[i] + 1:
					numOfJumps[j] = numOfJumps[i] + 1
					index[j] = i
		if i == j-1:
			i = 0
			j += 1
		else:
			i += 1
		
		if j == n-1 and i == n-2:
			break
	print 'Minimum number of jumps: ' + str(numOfJumps[-1])
	steps = [n-1]
	next = index[n-1]
	while next != -1:
		steps.append(next)
		next = index[steps[-1]]
	print 'Steps: ',steps[::-1]


if __name__ == '__main__':
	ar = [2,3,1,1,2,4,2,0,1,1]
	minimumJump(ar)