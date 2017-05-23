
def segmentation(candidate, words):
	final = []
	start, n = 0, 0
	while n <= len(candidate):
		#print start,n,candidate[start:n],final
		if candidate[start:n] in words:
			move = 0
			for i in range(n,len(candidate)+1):
				#print 'test', candidate[n:i]
				if candidate[n:i] in words:
					move = 1
					break
			if move == 1:
				final.append(candidate[start:n])
				start = n
				n = -1
		elif candidate[start:n].isdigit():
			for i in range(n,len(candidate)+1):
				if not candidate[start:i].isdigit():
					break
			final.append(candidate[start:i])
			start = i
			n = -1
		n += 1
	final.append(candidate[start::])
	
	print final
	# Choose the longest word
	output = []
	i = 0
	while i != len(final):
		if i < len(final)-1:
			if ''.join(final[i:i+2]) in words:
				output.append(''.join(final[i:i+2]))
				i += 1
			else:
				output.append(final[i])
		else:
			output.append(final[i])
		i += 1		
		
	print ' '.join(output)
	
if __name__ == '__main__':
	fid = open('words.txt')
	words = []
	for line in fid:
		words.append(line.replace('\n',''))

	t = int(raw_input())
	for _ in xrange(t):
		line = raw_input()
		if '.' in line:
			line = line.split('.')
			if 'www.' == line[0:4]:
				candidate = line[1]
			else:
				candidate = line[0]
		elif line[0] == '#':
			candidate = line[1::]
		segmentation(candidate, words)