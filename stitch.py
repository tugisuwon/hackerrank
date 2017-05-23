from sklearn.feature_extraction.text import TfidfVectorizer
def stitch(data,n):
	vectorizer = TfidfVectorizer(min_df=1)
	tf = vectorizer.fit_transform(data)
	s = (tf * tf.T)
	print s
	output = {}
	usedA = set()
	usedB = set()
	vals = [(-s[i,n+j], i, j) for i in range(n) for j in range(n)]
	print sorted(vals)
	for v,i,j in sorted(vals):
		print v,i,j
		if i in usedA or j in usedB: continue
		print usedA, usedB
		usedA.add(i)
		usedB.add(j)
		output[i]=j
	print output
	print usedA
	print usedB
if __name__ == "__main__":
    n = 2
    data = ["Hello I am Su Won Bae. Su Bae is short version.","Hi who are you",'My name is Sung Bae','How do you do? May I know your name?']
    stitch(data,n)