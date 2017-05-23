#!python2
from random import randint
import time

s = time.time()
'''
fid = open('temp.out','w')

d = '0123456789'
for _ in range(10**3):
	#print(randint(0,9), d[randint(0,9)])
	#print(''.join(d[randint(0,9)] for j in range(10))+'\r\n')
	fid.write(''.join(d[randint(0,9)] for j in range(10**4)) + '\n')
fid.close()
'''
a = []
fid = open('temp.out')
for i in fid:
	a.append(int(i))

b = sorted(int(x) for x in a)
print(time.time() - s)