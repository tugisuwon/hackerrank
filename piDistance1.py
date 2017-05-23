#!/bin/python

import sys


a = 99999
b = 222222
# your code goes here
from math import pi
d,e = 0,1
pa = [1, 7, 106, 113, 33102, 33215, 66317, 99532, 265381, 364913, 1360120, 1725033, 25510582, 52746197, 78256779, 131002976, 340262731, 811528438, 1963319607, 4738167652, 6701487259, 567663097408, 1142027682075, 1709690779483, 2851718461558, 44485467702853]
check = [x for x in pa if a<=x<=b]
if check != []:
    for i in check:
        t = pi*i
        p = abs(int(round(t))-t)
        if p < e:
            e = p
            d = [int(round(t)),i]
else:
	#i = a
	oo = 0
	for i in range(a,b+1):
		t = pi*i
		p = abs(int(round(t))-t)
		if p < e:
			if d != 0:
				print(i-d[1])
				if i - d[1] in pa[3:]:
					oo = 1
			e = p
			d = [int(round(t)),i]
		if oo == 1:
			break
			
	while i <= b:
		pp = [x for x in pa if x <= (b-i)]
		if pp != []:
			tt = [(i+j)*pi for j in pp]
			aa = [abs(int(round(x))-x) for x in tt]
			cc = min(aa)
			bb = aa.index(cc)
			i += pp[bb]
			if cc < e and i <= b:
				print(i, pp[bb])
				e = cc
				d = [int(round(tt[bb])), i]
		else:
			break
print(str(d[0])+'/'+str(d[1]))
