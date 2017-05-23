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
	
	bay_yes,bay_no = {},{}
	for i in contest:
		bay_yes[i] = {}
		bay_no[i] = {}
	
	# create semi-naive-bayesian dictionary to keep track of user's history. Two dictionaries are created: one for solved one and anotoher one for not-solved one. 
	dict_present = 0
	if dict_present == 0:
		for i in id:
			temp = df_submission['challenge_id'][df_submission['hacker_id']==i].values
			solved = df_submission['solved'][df_submission['hacker_id']==i].values
			challenged = []
			'''
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
			'''
			pre,pre_solved = temp[0],solved[0]
			for j in xrange(1,len(temp)):
				jj = temp[j]
				if pre_solved == 1:
					if jj in bay_yes[pre]:
						bay_yes[pre][jj] += 1
					else:
						bay_yes[pre][jj] = 1
				else:
					if jj in bay_no[pre]:
						bay_no[pre][jj] += 1
					else:
						bay_no[pre][jj] = 1
				pre = jj
				pre_solved = solved[j]
		with open('temp_yes.json','w') as f:
			json.dump(bay_yes,f)
		with open('temp_no.json','w') as f:
			json.dump(bay_no,f)
	else:
		with open('temp_yes.json') as f:
			bay_yes = json.load(f)
		with open('temp_no.json') as f:
			bay_no = json.load(f)
			
	con = df_challenge.contest_id.unique()
	bayes = {}
	for i in con:
		temp = df_challenge['challenge_id'][df_challenge['contest_id']==i].values
		temp1 = df_challenge['difficulty'][df_challenge['contest_id']==i].values
		y = []
		for iii in xrange(len(temp)):
			y.append((temp[iii],temp1[iii]))
		bayes[i] = y
		
	#difficulty 
	difficulty = {}
	for i in contest:
		difficulty[i] = df_challenge['difficulty'][df_challenge['challenge_id'] == i].values[0]
	
	df = df_challenge.sort('total_submissions_count', ascending=False).head(100)
	common = df['challenge_id'].values
	#print common
	
	print 'dict complete'
	output = []
	#no fancy math is involved, but rather a conditional probabilty + historical naive-bayesian dictionary. Looking at each user to see which set of problems that specific user was able to solve and suggest next set of problems 
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
			#solve -= 0.1
		if nns > 0:
			noSolve /= nns
			#noSolve += 0.1

		for yy in notSolved:
			if difficulty[yy] <= noSolve and yy not in solved:
				tt.append(yy)
			if len(tt) == 3:
				break

		candidate = {}
		visited = []
		for j in temp1:
			check = [temp3[oo] for oo in xrange(len(temp3)) if temp2[oo] == j]
			if 1 in check:
				t = sorted(bay_yes[j].items(), key=operator.itemgetter(1), reverse=True)
			else:
				t = sorted(bay_no[j].items(), key=operator.itemgetter(1), reverse=True)
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