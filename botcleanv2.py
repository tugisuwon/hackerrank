#!/usr/bin/python
import math
def distanceCalculator(a,b):
    return int(math.fabs(a[0]-b[0]) + math.fabs(a[1]-b[1]))

def next_move(posr, posc, board):
    bot = [posr, posc]
    dirty = []
    for i, item in enumerate(board):
        for j, item in enumerate(item):
            if item == 'd':
                dirty.append([i,j])
    if dirty == []:
        if posc < (j-1):
			print 'RIGHT'
		else:
			if posr < (i-1):
				print 'DOWN'
			elif posc > 1:
				print 'UP'
			else:
				print 'RIGHT'
    else:
        distance = []
        for item in dirty:
            distance.append(distanceCalculator([posr, posc],item))
        index = distance.index(min(distance))
        if bot == dirty[index]:
            print "CLEAN"
        else:
            output = []
            for i in range(0,2):
                move = dirty[index][i] - bot[i]
                while move != 0:
                    if i == 0:
                        if move > 0:
                            output.append('DOWN')
                            move -= 1
                        else:
                            output.append('UP')
                            move += 1
                    else:
                        if move > 0:
                            output.append('RIGHT')
                            move -= 1
                        else:
                            output.append('LEFT')
                            move += 1
            print output[0]

if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
