if __name__ == '__main__':
	paragraph = raw_input()
	candidates = paragraph.split('.')
	
	final = []
	n = 0
	temp = ''
	while n < len(candidates)-1:			
		temp += candidates[n].strip()
		if temp not in ['Dr','Mr','Mrs','Jr'] and len(temp) != 1 and temp.count('\"') % 2 == 0:
			if '!' in temp or '?' in temp:
				breaker = [x for x in xrange(len(temp)) if temp[x] in ['!','?']]
				start = 0
				if '\"' in temp:
					quotation = [x for x in xrange(len(temp)) if temp[x] == '\"']
					for i in breaker:
						tt = [x for x in xrange(len(quotation)/2) if quotation[2*x] < i and quotation[2*x+1] > i]
						if tt == []:
							last = temp[start:i+1].strip()
							if last[-1] not in ['!','?']:
								last += '.'
							final.append(last)
							start = i + 1
				else:
					for i in breaker:
						final.append(temp[start:i+1].strip())
						start = i + 1
				last = temp[start::].strip()
				if '?' not in last and '!' not in last:
					last += '.'
				final.append(last)
			else:
				final.append(temp.strip()+'.')
			temp = ''
		n += 1
	next = 0
	for line in final:
		if line[-1] not in ['!', '?'] and line[-1] != '.':
			line += '.'
		if next == 0:
			if line.count('\'' ) % 2 != 0:
				line += '\''
				next = 1
		else:
			line = line.replace('\'','').strip()
			next = 0
		print line