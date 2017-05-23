
min=8
max=100

from math import pi

pa = [1, 7, 106, 113, 33102, 33215, 66317, 99532, 265381, 364913, 1360120, 1725033, 25510582, 52746197, 78256779, 131002976, 340262731, 811528438, 1963319607, 4738167652, 6701487259, 567663097408, 1142027682075, 1709690779483, 2851718461558, 44485467702853]
for i in pa:
	t = pi*i
	p = abs(int(round(t))-t)
	print(i,p)
d,e = [0,0],1
output = []
for i in range(min,max+1):
	t = pi*i
	p = abs(int(round(t))-t)
	if p < e:
		print(i,i-d[1])
		e = p
		d = [int(round(t)),i]
	output.append(p)
print(d)
'''
#print(output[:20])
diff = [(output[i+1]-output[i]) > 0 for i in range(len(output)-1)]
s = True
k = 1
out = []
temp = []
for i in diff:
	if i != s:
		#out.append((s,k))
		if s == True:
			temp.append(k)
			s = False
		else:
			temp.append(k)
			out.append(temp)
			temp = []
			s = True
		k = 1
	else:
		k += 1
a = [(x,(x-7)/16) for x in range(len(out)) if out[x] == [4,4]]
p = 0
pp = []
for i in a:
	b = i[1]-int(i[1])
	if b != p:
		pp.append(i[0])
		p = b
print(pp)
'''