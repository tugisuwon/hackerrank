fid = open('solution.txt', 'rb')


	
		
line = fid.readlines()
first = line[0].replace('\r\n','')
second = line[1].replace('\r\n','')
solution = line[2].replace('\r\n','')

output = ''
while first != '' and second != '':
	if first == second:
		output = ''.join([x*2 for x in first])
		first, second = '', ''
	else:
		a, b = first[0], second[0]
		if ord(a) < ord(b):
			output += a
			first = first[1::]
		elif ord(a) > ord(b):
			output += b
			second = second[1::]
		elif ord(a) == ord(b):
			order = 1
			while True:
				if ord(first[order]) < ord(second[order]):
					output += a
					first = first[1::]
					break
				elif ord(first[order]) > ord(second[order]):
					output += b
					second = second[1::]
					break
				else:
					order += 1
				if order == len(first) or order == len(second):
					output += a
					first = first[1::]
					break
				if order > 3:
					couple = enumerate(zip(first, second))
					index = [x for x, (f, s) in couple if f != s]
					if index == []:
						output += a
						first = first[1::]
						break
		if output != solution[0:len(output)]:
			print first[0:5]
			print second[0:5]
			print output
			print solution[0:len(output)]
			a = raw_input('a')
		if first == '':
			output += second
			second = ''
		elif second == '':
			output += first
			first = ''
print output