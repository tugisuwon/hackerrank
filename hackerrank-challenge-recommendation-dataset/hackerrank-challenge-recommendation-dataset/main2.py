import pandas as pd
import operator
import json

def preprocessing(df):
	return 0


def main():
	df_challenge = pd.read_csv('challenges.csv')
	df_submission = pd.read_csv('submissions.csv')
	
	id = df_submission.hacker_id.unique()
	contest = df_challenge.challenge_id.unique()
	
	bay = {}
	for i in contest:
		bay[i] = {}
	
	dict_present = 1
	if dict_present == 0:
		for i in id:
			temp = df_submission['challenge_id'][df_submission['hacker_id']==i].values
			solved = df_submission['solved'][df_submission['hacker_id']==i].values
			for j in temp:
				for k in temp:
					if j != k:
						if k in bay[j]:
							bay[j][k] += 1
						else:
							bay[j][k] = 1
						if j in bay[k]:
							bay[k][j] += 1
						else:
							bay[k][j] = 1
		with open('temp1.json','w') as f:
			json.dump(bay,f)
	else:
		with open('temp1.json') as f:
			bay = json.load(f)
	
	con = df_challenge.contest_id.unique()
	bayes = {}
	for i in con:
		temp = df_challenge['challenge_id'][df_challenge['contest_id']==i].values
		temp1 = df_challenge['difficulty'][df_challenge['contest_id']==i].values
		y = []
		for iii in xrange(len(temp)):
			y.append((temp[iii],temp1[iii]))
		bayes[i] = y
		
	#print bayes
	difficulty = {}
	for i in contest:
		difficulty[i] = df_challenge['difficulty'][df_challenge['challenge_id'] == i].values[0]
	
	df = df_challenge.sort('total_submissions_count', ascending=False).head(100)
	common = df['challenge_id'].values
	#print common
	
	print 'dict complete'
	output = []
	for i in id:
		tt = [i]
		temp = df_submission[df_submission['hacker_id']==i]
		temp1 = temp['challenge_id'].unique()
		temp2 = temp['challenge_id'].values
		temp3 = temp['solved'].values
		temp4 = temp['contest_id'].unique()
		solved = []
		notSolved = []
		solve,noSolve = 0,0
		ns,nns = 0,0
		for k in xrange(len(temp1)):
			#print k,temp2[k]
			temp_k = [temp3[xx] for xx in xrange(len(temp3)) if temp2[xx] == temp1[k]]
			if 1 in temp_k:
				solved.append(temp1[k])
				ns += 1
				solve += difficulty[temp1[k]]
			else:
				notSolved.append(temp1[k])
				nns += 1
				noSolve += difficulty[temp1[k]]
		if ns > 0:
			solve /= ns
			solve -= 0.1
		if nns > 0:
			noSolve /= nns
			noSolve += 0.1
		
		for yy in notSolved:
			if difficulty[yy] <= noSolve:
				tt.append(yy)
			if len(tt) == 5:
				break

		candidate = {}
		visited = []
		for j in temp1:
			t = sorted(bay[j].items(), key=operator.itemgetter(1), reverse=True)
			for ii in t:
				if ii not in visited:
					if ii[0] not in candidate:
						candidate[ii[0]] = ii[1]
					else:
						candidate[ii[0]] += ii[1]
			visited.append(j)
			
		t = sorted(candidate.items(), key=operator.itemgetter(1), reverse=True)
		for jj in t:
			if jj[0] not in solved and jj[0] not in tt:
				if solve != 0 and noSolve != 0:
					if difficulty[jj[0]] >= solve or difficulty[jj[0]] <= noSolve:
						tt.append(jj[0])
				elif solve == 0:
					if difficulty[jj[0]] <= noSolve:
						tt.append(jj[0])
				else:
					if difficulty[jj[0]] >= solve:
						tt.append(jj[0])
			if len(tt) >= 11:
				break
		if len(tt) < 11:
			print i
			print tt,len(tt)
			for kk in temp4:
				temp_ = bayes[kk]
				if solve != 0 and noSolve != 0:
					tt += [temp_[a][0] for a in xrange(len(temp_)) if (temp_[a][1] <= noSolve or temp_[a][1] >= solve) and temp_[a][0] not in tt and temp_[a][0] not in solved]
				elif solve == 0:
					tt += [temp_[a][0] for a in xrange(len(temp_)) if temp_[a][1] <= noSolve and temp_[a][0] not in tt and temp_[a][0] not in solved]
				else:
					tt += [temp_[a][0] for a in xrange(len(temp_)) if temp_[a][1] >= solve and temp_[a][0] not in tt and temp_[a][0] not in solved]
			if len(tt) < 11:
				for to in common:
					if to not in solved and to not in tt:
						if solve != 0 and noSolve != 0:
							if difficulty[to] >= solve or difficulty[to] <= noSolve:
								tt.append(to)
						elif solve == 0:
							if difficulty[to] <= noSolve:
								tt.append(to)
						else:
							if difficulty[to] >= solve:
								tt.append(to)
					if len(tt) == 11:
						break
		elif len(tt) > 11:
			print i
			print tt
			a = raw_input('a')
		tt = tt[:11]
		output.append(tt)
	
	output_file = open('recommendation.csv','wb')
	for i in output:
		output_file.write(','.join(i)+'\r\n')
		


if __name__ == '__main__':
	main()