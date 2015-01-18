numcases = input()

result = []
primes = [2,3,5,7]

for n in xrange(numcases):
    num = input()
    lastPrime = 0
    for i in xrange(2,num+1):
        print 'num',num, lastPrime,i
        newPrime = False
        if num % i == 0:
            #got divisor
            # now check if it is a prime or not
            if i in primes:
                lastPrime = i
                continue
            else:# not in the primes list, need to add
                for j in primes:
                    if i % j == 0:
                        # not a prime
                        lastPrime = j
                        newPrime = False
                        print 'in j loop lastprime',lastPrime,j
                        continue
                        
                    else:
                        if newPrime == False:
                            # it is divisor but not prime
                            break
                        newPrime = True

                if newPrime:
                    primes.append(i)
                    lastPrime = i
        print 'Last prime',lastPrime
    result.append(lastPrime)

for r in result:
    print lastPrime
