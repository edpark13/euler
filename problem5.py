def smallest_multiple(n):
    primes = []
    for i in xrange(2, n):
        print "i is " + str(i)
        largest_prime = 0
        for j in xrange(2, i):
            print "j is " + str(j)
            if i % j == 0: 
                print str(j) + " goes into " + str(i) + " evenly"
                largest_prime = j
        if largest_prime == 0:
            primes.append(i)
        else:
            primes.append(largest_prime)
    print primes
    result = 1
    for prime in primes:
        result *= prime
    return result

if __name__ == '__main__':
    print smallest_multiple(10)
