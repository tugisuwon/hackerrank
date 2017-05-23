# Enter your code here. Read input from STDIN. Print output to STDOUT
def findAll(n,road):
    output = []
    forward = [1]
    current = [[1]]
    while True:
        if forward == []:
            break
        else:
            forward = []
            for i in current:
                #print current, i
                c = road[i[-1]]
                for j in [x for x in c if x not in i]:
                    if j == n:
                        output.append(i + [j])
                    else:
                        forward.append(i + [j])
            current = forward
    return output

if __name__ == '__main__':
    n,m,k = map(int,raw_input().split())
    fish = {}
    for ii in xrange(n):
        ar = map(int,raw_input().split())
        fish[ii+1] = ar[1:]
    road = {}
    road_time = {}
    for _ in xrange(m):
        ar = map(int,raw_input().split())
        if ar[0] in road:
            road[ar[0]].append(ar[1])
        else:
            road[ar[0]] = [ar[1]]
        if ar[1] in road:
            road[ar[1]].append(ar[0])
        else:
            road[ar[1]] = [ar[0]]
        road_time[(ar[0],ar[1])] = ar[2]
    
    # find all possible paths from 1 to n
    paths = findAll(n,road)
    
    time, fishNum = [], []
    for i in paths:
        f,t = [],0
        for j in xrange(len(i)):
            jj = i[j]
            print j,jj,fish[jj]
            f = list(set(f).union(fish[jj]))
            if jj != n:
                kk = i[j+1]
                if (jj,kk) in road_time:
                    t += road_time[(jj,kk)]
                else:
                    t += road_time[(kk,jj)]
        time.append(t)
        fishNum.append(f)
    order = [i[0] for i in sorted(enumerate(time), key=lambda x:x[1])]
    paths = [x for (y,x) in sorted(zip(order,paths))]
    fishNum = [x for (y,x) in sorted(zip(order,fishNum))]
    time.sort()
    
    # single journey case
    best = 0
    for n,i in fishNum:
        if max(len(i),)