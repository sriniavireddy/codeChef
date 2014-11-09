# n is the number of testcases
import sys
import math
n = int(sys.stdin.readline().rstrip())
x = []
y = []
for i in xrange(0,n):
    turns = int(sys.stdin.readline().rstrip())
    count = 0       
    x = [int(a) for a in sys.stdin.readline().rstrip().split()]
    y = [int(b) for b in sys.stdin.readline().rstrip().split()]
    x = sorted(x, reverse = True)
    y = sorted(y)
    for c in x:
        for d in y:
            if c < d
