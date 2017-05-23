#https://www.hackerrank.com/contests/w25/challenges/stone-division
# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int,raw_input().split())
s = map(int,raw_input().split())


def nim_sum(a): return reduce(lambda x, y: x ^ y, a, 0)

def mex(a):
    s = set(a)
    n = len(s)
    for i in xrange(n):
        if not i in s:
            return i
    return n

SG = {}
def sg(n):
    if n in SG: return SG[n]
    res = mex((nim_sum([sg(n/f)] * (f%2)) for f in s if n%f == 0))
    SG[n] = res
    return res

result = nim_sum(sg(n) for n in [n])
print ['First','Second'][result==0]