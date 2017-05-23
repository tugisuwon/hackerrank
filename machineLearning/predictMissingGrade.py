# Enter your code here. Read input from STDIN. Print output to STDOUT
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import PassiveAggressiveRegressor
from sklearn.ensemble import GradientBoostingRegressor
def vectorizer(x,y):
	#clf = RandomForestClassifier(n_estimators=100)
	#clf = PassiveAggressiveRegressor(epsilon=0.001)
	clf = GradientBoostingRegressor(loss = 'huber')
	clf.fit(x,y)
	return clf

if __name__ == '__main__':
	index = {'Physics':0,'Chemistry':1,'PhysicalEducation':2,'Biology':3,'ComputerScience':4,'BusinessStudies':5,'Economics':6,'Accountancy':7}
	with open('training.json') as f:
		t = int(f.readline())
		x,y = [], []
		for i in xrange(t):
			#print i
			x.append([0]*8)
			temp = json.loads(f.readline())
			#print temp
			for k,v in temp.iteritems():
				if k in index:
					x[i][index[k]] = v
				elif k == 'Mathematics':
					y.append(v)
		
	clf = vectorizer(x,y)
	'''
	with open('sample-test.in.json') as f:
		t = int(f.readline())
		x_test = []
		index = {'Physics':0,'Chemistry':1,'PhysicalEducation':2,'Biology':3,'ComputerScience':4,'BusinessStudies':5,'Economics':6,'Accountancy':7}
		for i in xrange(t):
			x_test.append([0]*8)
			temp = json.loads(f.readline())
			for k,v in temp.iteritems():
				if k in index:
					x_test[i][index[k]] = v
	y_predict = clf.predict(x_test)
	y_score = []
	with open('sample-test.out.json') as f:
		for _ in xrange(t):
			score = int(f.readline())
			y_score.append(int(y_predict[i]) - score)

	#print y_score
	print sum(y_score)
	'''
	t = int(raw_input())
	x_test = []
	for i in xrange(t):
		x_test.append([0]*8)
		temp = json.loads(raw_input())
		#print temp
		for k,v in temp.iteritems():
			if k in index:
				x_test[i][index[k]] = v
	
	y = clf.predict(x_test)
	for i in y:
		print int(i)
