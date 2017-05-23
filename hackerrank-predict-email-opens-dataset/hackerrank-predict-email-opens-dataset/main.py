import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import PassiveAggressiveClassifier, LogisticRegression
from sklearn.naive_bayes import MultinomialNB


def difference(x):
	return int(x[1]) - int(x[0])

def exist(x):
	return x > 0

def vectorizer(x,y,n=10):
	# choosing the model for this question. Because we are dealing with sparse matrix that may not be singular, each parameter must be sensitive to change. Several iteration may require for the best fit, but initially it's based on an educated guess
	#vectorizer = TfidfVectorizer(ngram_range=(1,2), sublinear_tf=True)
	
	#clf = PassiveAggressiveClassifier(n_iter=100) #0.33199
	#clf = MultinomialNB(alpha=0.05) #0.6012
	#clf = LogisticRegression() #0.6679
	#clf = LinearSVC(C=1.5) #0.4384
	clf = RandomForestClassifier(n_estimators=n) #0.9718
	
	#pipeline = Pipeline([('prep', vectorizer), ('clf', clf)])
	
	clf.fit(x, y)
	#print clf.score(x,y)
	return clf
def preprocessing(df):
	#replace all nan to 0
	df = df.fillna(0)
	
	#categorize by user_id
	#id = df.user_id.unique()
	columnNames = list(df.columns.values)
	n = df.shape[0]
	df['diff'] = [0]*n
	df['diff'] = df['sent_time'].values - df['last_online'].values
	category = []
	h = 'mail_category_'
	for i in xrange(1,19):
		category.append(h+str(i))
	#print category
	
	#to study general case, ignoring user_id: by converting mail_category into sparse matrix, we can investigate the correlation between "opened" and mail category
	for i in category:
		df[i] = [0]*n
	df['mail_null'] = [0]*n
	for i in xrange(n):
		temp = df['mail_category'].iloc[i]
		#print temp
		if temp != 0:
			df[temp].iloc[i] = 1
		else:
			df['mail_null'].iloc[i] = 1
	
	#to study any correlation between recent activities and "opened", we need to create another spare matrix based on recent activities of each user
	
	#we need to change the data type of certain columns to prevent round-off erros
	df[['contest_participation_count_7_days','contest_participation_count']] = df[['contest_participation_count_7_days','contest_participation_count']].astype(float)
	df['contest_participation'] = df['contest_participation_count_7_days'].values / df['contest_participation_count'].values
	#print df['contest_participation'].iloc[:10]
	
	df[['contest_login_count_7_days','contest_login_count']] = df[['contest_login_count_7_days','contest_login_count']].astype(float)
	df['contest_login'] = df['contest_login_count_7_days'].values / df['contest_login_count'].values
	
	df[['ipn_count_7_days','ipn_count_1_days','ipn_count','ipn_read','ipn_read_1_days','ipn_read_7_days']] = df[['ipn_count_7_days','ipn_count_1_days','ipn_count','ipn_read','ipn_read_1_days','ipn_read_7_days']].astype(float)
	df['ipn_count_7'] = df['ipn_read_7_days'].values / df['ipn_count_7_days'].values
	df['ipn_count_1'] = df['ipn_read_1_days'].values / df['ipn_count_1_days'].values
	df['ipn_count_all'] = df['ipn_read'].values / df['ipn_count'].values
	
	#boolean
	df['forum_comment'] = df['forum_comments_count'].map(lambda x: exist(x))
	df['forum'] = df['forum_count'].map(lambda x: exist(x))
	df['forum_expert'] = df['forum_expert_count'].map(lambda x: exist(x))
	df['forum_question'] = df['forum_questions_count'].map(lambda x: exist(x))
	
	#dropping columns we don't want
	keep = ['user_id','opened']
	column = []
	for i in columnNames:
		if i not in keep:
			column.append(i)
	df.drop(column,inplace=True,axis=1)
	return df

def idConvert(x,mapping):
	if x in mapping:
		return mapping[x]
	else:
		return 0

def prediction(x_train,y_train,x_test):
	y_test = []
	pre = ''
	for i in xrange(len(x_test)):
		x = x_test.iloc[i]['user']
		if pre != x:
			if x != 0:
				index = x_train[x_train['user']==x].index.tolist()
				xx,yy =x_train.loc[index],[y_train[j] for j in index]
			else:
				xx,yy =x_train,y_train
			clf = vectorizer(xx,yy)
		#print 'result', clf.predict(x_test.iloc[i])
		pre = x
		y_test.append(clf.predict(x_test.iloc[i]))
		if i % 5000 == 0:
			print i,pre,x
	return y_test
		
		
def main():
	preprocess = 0
	if preprocess == 1:
		nr = 0
		if nr != 0:
			df = pd.read_csv('training_dataset.csv',nrows=1000)
		else:
			df = pd.read_csv('training_dataset.csv')
		
		df = preprocessing(df)
		
		df = df.fillna(0)
		#save it to csv
		df.to_csv('temp.csv',sep=',')
	else:
		df = pd.read_csv('temp.csv')
		
	id = df.user_id.unique()
	mapping = {}
	
	dropList = ['opened','user_id','Unnamed: 0','ipn_count_all','ipn_count_1']
	
	for j in xrange(len(id)):
		mapping[id[j]] = j+1
	#define x and y train list
	y_train = df['opened'].values
	df['user'] = df['user_id'].map(lambda x: idConvert(x,mapping))
	df.drop(dropList,inplace=True,axis=1)
	print list(df.columns.values)
	
	x_train = df[:]
	#print x_train[:10]
	
	#choose the model for regression
	#clf = vectorizer(x_train,y_train,len(id)+1)
	
	#read test file
	preprocess = 0
	if preprocess == 1:
		df_test = pd.read_csv('test_dataset.csv')
		df_test = preprocessing(df_test)
		df_test = df_test.fillna(0)
		df_test.to_csv('temp_test.csv',sep=',')
	else:
		df_test = pd.read_csv('temp_test.csv')
	df_test['user'] = df_test['user_id'].map(lambda x: idConvert(x,mapping))
	df_test = df_test.sort(['user'],ascending=[True])
	print df_test[:30]
	#a = raw_input('a')
	df_test.drop(dropList[1::],inplace=True,axis=1)
	x_test = df_test[:]
	#print list(df_test.columns.values)
	#apply model to test data
	#y_test = clf.predict(x_test)
	print len(x_test[x_test['user']==0].index.tolist())
	print x_test.shape
	a = raw_input('a')
	y_test = prediction(x_train,y_train,x_test)
	
	output = open('prediction.csv','wb')
	for i in y_test:
		j = 0
		if i == True:
			j = 1
		output.write(str(j)+'\r\n')
	'''
	for i in id:
		x = [0] * 18
		y = [0] * 18
		t = df.loc[df['user_id'] == i]
		t = t.sort(['sent_time'], ascending=[1])
		tt = t['mail_category'].values
		uu = t['opened'].values
		#print tt
		for j in xrange(len(tt)):
			print tt[j]
			x[category.index(tt[j])] += 1
			if uu[j] == True:
				y[category.index(tt[j])] += 1
		z = []
		for k in xrange(len(x)):
			if x[k] != 0:
				z.append(y[k]/float(x[k]))
			else:
				z.append(0)
		print i,z
		print t[['user_id','sent_time','last_online','mail_category','opened','diff']]
		a = raw_input('a')
	'''


if __name__ == '__main__':
	main()