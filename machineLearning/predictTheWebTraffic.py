# Enter your code here. Read input from STDIN. Print output to STDOUT
import statsmodels.api as st

N, past_num, week_num = input(), 154, 7
data = [input() for _ in xrange(N)]

X = [[i] + [1 if j == i % week_num else 0 for j in xrange(week_num)] for i in xrange(N - past_num, N)]
Y = data[-past_num:]

model = st.OLS(Y, X).fit()

X = [[N + i] + [1 if j == (N + i) % week_num else 0 for j in xrange(week_num)] for i in xrange(30)]
for i in model.predict(X):
    print i - 6