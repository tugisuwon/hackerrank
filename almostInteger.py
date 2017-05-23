a = {(i**2+j**2)**0.5:(i,j) for i in range(1,13) for j in range(i,13) if (i,j) not in [(12,9),(12,5),(9,12),(8,6),(6,8),(5,12),(3,4),(4,3),(1,11),(2,12),(4,5),(3,12),(3,10),(6,9),(7,12),(6,6),(4,12),(7,11)]}
#a = {(i**2+j**2)**0.5:(i,j) for i in range(1,13) for j in range(i,13) if (i,j) in [(1,11),(2,12),(4,5),(3,12),(3,10),(6,9),(7,12),(6,6),(4,12),(7,11)]}
c = {j:i for i,j in a.items()}
from itertools import combinations
from random import shuffle
b = [i for _ in range(3) for i,j in a.items()]
shuffle(b)
#print(b)
#print b
ll = 0
for k in combinations(b,12):
	temp = sum(k)
	temp = abs(temp-int(temp))
	#print(temp,temp%1)
	if temp <= 10**-10:
		print("found")
	if temp <= 10**-12:
		output = []
		for j in k:
			output.append(a[j])
		print(output)
	ll += 1
	if ll % 100000000 == 0:
		print(ll)