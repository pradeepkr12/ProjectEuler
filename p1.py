numcases = input()

def numOfDivisor(a,b):
    return a*b*(b+1)/2
res = []
for i in xrange(0,numcases):
    n = input()
    n -= 1

    n1 = n/3
    n2 = n/5
    n3 = n/15
    s1 = numOfDivisor(3,n1)
    s2 = numOfDivisor(5,n2)
    s3 = numOfDivisor(15,n3)
    res.append(s1+s2-s3)

for r in res:
    print r


