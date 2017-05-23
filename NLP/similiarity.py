import math
d1 = "I d like an apple"
d2 = "An apple a day keeps the doctor away"
d3 = "Never compare an apple to an orange"
d4 = "I prefer scikit learn to orange"

docs = [d1, d2, d3, d4]
tfidf = [0,0,0,0]
for dx in range(4):
	for word in docs[dx].split():
		d = 0
		print dx, word, docs[:dx] + docs[dx+1:]
		for doc in docs[:dx] + docs[dx+1:]:
			if word in doc:
				d += 1
        tfidf[dx]+= math.log(4/(1+d))
print tfidf
ans = [abs(num - tfidf[0]) for num in tfidf]
print ans.index(min(ans[1:]))+1