import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import PassiveAggressiveClassifier, LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from datetime import datetime
import numpy as np

def difference(x):
	return int(x[1]) - int(x[0])

def exist(x):
	return x > 0

def vectorizer(x,y,n=50):
	# choosing the model for this question. Because we are dealing with sparse matrix that may not be singular, each parameter must be sensitive to change. Several iteration may require for the best fit, but initially it's based on an educated guess
	#vectorizer = TfidfVectorizer(ngram_range=(1,2), sublinear_tf=True)
	
	#clf = PassiveAggressiveClassifier(n_iter=100) #0.33199
	#clf = MultinomialNB(alpha=0.05) #0.6012
	#clf = LogisticRegression() #0.6679
	#clf = LinearSVC(C=1.5) #0.4384
	clf = RandomForestClassifier(n_estimators=n) #0.9718
	#clf = DecisionTreeRegressor(max_depth=20)
	#clf = AdaBoostClassifier(n_estimators=100)
	#clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
	#pipeline = Pipeline([('prep', vectorizer), ('clf', clf)])
	
	clf.fit(x, y)
	print clf.score(x,y)
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
	# This is to create a dictionary with key-value of user_id and its assigned dimension
	if x in mapping:
		return mapping[x]
	else:
		return 0

def prediction(x_train,y_train,x_test):
	# This function computes the prediction by user_id specific. Very slow approach, but was used to test the correlation between user_id and "opened" variable
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
		
def type(x):
	if x == 0:
		return 0
	else:
		return int(x[-1])

def weekday(x):
	if x == 0:
		return 0
	else:
		week = {'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
		return week[datetime.fromtimestamp(x/1000).strftime("%A")]
		
def preprocessing1(df,columnNames):
	df = df.fillna(0)
	df['timezone'] = df['hacker_timezone'] / 3600
	#df['mailtype'] = df['mail_type'].map(lambda x:type(x))
	#df['mailcategory'] = df['mail_category'].map(lambda x:type(x))
	#df['weekday'] = df['sent_time'].map(lambda x:weekday(x))
	df['forum'] = df['forum_comments_count'].values + df['forum_count'].values + df['forum_expert_count'].values + df['forum_questions_count'].values
	#df['submission'] = df['submissions_count'].values + df['submissions_count_contest'].values + df['submissions_count_master'].values
	#df['ipn'] = df['ipn_read'].values/df['ipn_count'].values*100
	#df['diff'] = (df['sent_time'].values - df['last_online'].values)/3600
	#print df[:10]	
	#dropping columns we don't want
	
	keep = ['user_id','opened']
	#keep = ['user_id','contest_login_count','contest_participation_count','submissions_count','opened']
	column = []
	for i in columnNames:
		if i not in keep:
			column.append(i)
	df.drop(column,inplace=True,axis=1)
	return df
		
def main():
	df = pd.read_csv('training_dataset.csv')
	columnNames = list(df.columns.values)
	#print columnNames
	df = preprocessing1(df,columnNames)
		
	id = df.user_id.unique()
	mapping = {}
	
	dropList = ['opened','user_id']
	
	for j in xrange(len(id)):
		mapping[id[j]] = j+1
		
	#define x and y train list
	y_train = df['opened'].values
	
	df['user'] = df['user_id'].map(lambda x: idConvert(x,mapping))

	#manual intervention
	manual = 0
	allOpen = []
	allNotOpen = []
	if manual == 1:
		for i in id:
			temp = df['opened'][df['user_id']==i].values
			unique,counts = np.unique(temp, return_counts=True)
			tt = dict(zip(unique,counts))
			if 1 not in tt:
				tt[1] = 0
			if tt[1]/float(len(temp)) >= 0.95:
				allOpen.append(mapping[i])
			elif tt[1]/float(len(temp)) <= 0.05:
				allNotOpen.append(mapping[i])

	#print allOpen
	#print allNotOpen
	#print df[:10]
	df.drop(dropList,inplace=True,axis=1)
	print list(df.columns.values)
	x_train = df[:]
	#print x_train[:10]
	
	#choose the model for regression
	#clf = vectorizer(x_train,y_train,len(id)+1)
	
	#read test file

	df_test = pd.read_csv('test_dataset.csv')
	columnNames = list(df_test.columns.values)
	df_test = preprocessing1(df_test,columnNames)
	#df_test['unsubscribed'] = [0]*df_test.shape[0]
	id = df_test.user_id.unique()
	j = len(mapping)
	for i in xrange(len(id)):
		if id[i] not in mapping:
			mapping[id[i]] = j+1
			j += 1
	
	df_test['user'] = df_test['user_id'].map(lambda x: idConvert(x,mapping))
	
	df_t = df_test['user']
	
	df_test.drop(dropList[1::],inplace=True,axis=1)
	x_test = df_test[:]
	#print list(df_test.columns.values)
	#apply model to test data
	#y_test = clf.predict(x_test)
	clf = vectorizer(x_train,y_train)
	y_test = clf.predict(x_test)
	
	output = open('prediction.csv','wb')
	for j,i in enumerate(y_test):
		us = df_t[j]
		if us in allOpen:
			j = 1
		elif us in allNotOpen:
			j = 0
		else:
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