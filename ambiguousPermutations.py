import sys

n = int(sys.stdin.readline().rstrip())

while n!= 0:
    hashmap = []
    index = 1
    flag = 0
    hashmap = [int(x) for x in sys.stdin.readline().rstrip().split()]
    for i in xrange(0,(n+1)/2):
        if i+1 != hashmap[hashmap[i]-1]:
            flag = -1 
            break
    if flag == -1:
        print 'not ambiguous'
    else:
        print 'ambiguous'
    n = int(sys.stdin.readline().rstrip())
