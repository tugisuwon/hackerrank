import time

start = time.time()

S = 'SOSSPSSQSSORSOSSPSSQSSORSOSSPSSQSSORSOSSPSSQSSORSOSSPSSQSSORSOSSPSSQSSOR'
output = 0
for i in xrange(0,len(S)/3+1):
    output += sum(a!=b for a, b in zip(S[3*i:3*i+3], 'SOS'))
print output
print time.time() - start