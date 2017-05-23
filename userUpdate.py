import urllib2

users = ['tugisuwon','yunhuchoi','bryan238','jpark2320','sh87tuck','mlee432','nuppan','jangandsim']
table = []
for user in users:

	#response = urllib2.urlopen('https://www.hackerrank.com/leaderboard/algorithms/contest/level/1/filter/hacker='+user+'/page/1')
	response = urllib2.urlopen('https://codefights.com/profile/'+user)
	html = response.read()
	output = open('temp','wb')
	output.write(html)
	print html
	a = raw_input('a')
	
