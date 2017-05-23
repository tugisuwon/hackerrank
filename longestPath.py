def longestPath(ci, parent, N):
    length = [0]*(N)
    for i in xrange(N):
        if i == 0:
            length[0] = 1
        else:
            if ci[i] == 1:
                length[i] = length[parent[i]-1] + 1
    print length
    for j in xrange(N-1,0,-1):
		if parent[j] > j:
			length[j] = length[j] + length[parent[j]-1]
    print length

    print max(length)

N = 5
ci = [1, 1, 1, 0, 1]
parent = [0, 3, 1, 2, 1]
longestPath(ci, parent, N)