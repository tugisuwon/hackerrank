def biggerIsGreater(line,t):
    changed = 0
    for i in range(len(line)-1,len(line)-t-1,-1):
        for j in range(len(line)-2,len(line)-t-2,-1):
            #print line,i,j
			if i > j and ord(line[i]) > ord(line[j]):
				print i,j,line
				first, second = line[i], line[j]
				line[i] = second
				line[j] = first
				changed = 1
				temp = line[0:j+1] + sorted(line[j+1::])
				break
        if changed == 1:
            break
    #print changed           
    if changed == 0:
        if t != len(line)-1:
            t += 1
            biggerIsGreater(line,t)
        else:
            print 'no answer'
    else:
        #print temp
        output = ''.join(temp)
        print output


fid = open('biggerIsGreater.txt','rb')
output = open('solution.txt','rb')
solution = []
for ll in output:
	solution.append(ll.replace('\r\n',''))
n = 0
for line in fid:
	print line, n
	if biggerIsGreater(list(line.replace('\r\n','')),0) != solution[n]:
		print biggerIsGreater(list(line.replace('\r\n','')),0)
		print solution[n]
		a = raw_input('a')
	n += 1
	#a = raw_input('a')