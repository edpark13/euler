from math import sqrt

def summation_of_primes(num):
    """
    Find the sum of all the primes numbers less than the given number
    """
    sum = 0
    for i in xrange(2, num):
        for j in xrange(2, int(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            print i
            sum += i
    return sum

if __name__ == '__main__':
    print summation_of_primes(2000000)
