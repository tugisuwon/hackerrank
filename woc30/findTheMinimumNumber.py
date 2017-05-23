#!/bin/python
#https://www.hackerrank.com/contests/w30/challenges/find-the-minimum-number/submissions/code/1300902155
import sys


n = int(raw_input().strip())
print 'min(int, '*(n-2) + 'min(int, int)' + ')'*(n-2)