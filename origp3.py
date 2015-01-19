# numcases = input()

def solve():
	result = []
	primes = [2,3,5,7]
	numcases = 50
	for n in xrange(2,numcases):
	    # num = input()
	    num = n
	    lastPrime = 0
	    newPrime = False
	    notPrime = False
	    # check if it is prime
	    for p in primes:
	    	if num < p:
	    		break
	    	if num % p == 0:
	    		lastPrime = p
	    		notPrime = True
	    	else:
	    		if notPrime == True:
	    			newPrime = False
	    		else:
	    			newPrime = True
	    		# lastPrime = p
	    if newPrime and num > primes[-1]:
	    	primes.append(num)
	    	lastPrime = num

	    result.append(lastPrime)



	for i,r in enumerate(result):
	    print i+2,r

solve()
                    
                        

