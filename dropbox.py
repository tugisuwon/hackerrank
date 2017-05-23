def losslessDataCompression(inputString, width):
	i,index = 0,0
	output = ''
	#inputString = [x for x in inputString]
	while True:
		print max(index-width,0),min(index,index+width)
		window = inputString[max(index-width,0):min(index,index+width)]
		print 'w', window, output, index
		if inputString[index] in window:
			k = 2
			while True:
				print inputString[index:index+k],i,k
				if inputString[index:index+k] in window:
					k += 1
				else:
					break
				if index+k > len(inputString):
					break
			k -= 1
			print index, index+k+1, inputString[index:index+k],'c'
			i = inputString.index(inputString[index:index+k],max(index-width,0))
			index += k
			temp = (i,k)
			print str(temp).replace(' ',''),k
			output += str(temp).replace(' ','')
		else:
			output += inputString[index]
			index += 1
		if index >= len(inputString):
			break
	print output
	return output

losslessDataCompression('abacabadabacaba',7)