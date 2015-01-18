numcases = input()

result = []
for i in xrange(numcases):
    num = input()

    fib3,fib6 = 2,0
    res = 0

    while res < num:
        res = 4*fib3 + fib6
        fib6, fib3 = fib3, res

    result.append(res)

for r in result:
    print r
