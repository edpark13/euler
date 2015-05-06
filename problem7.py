from math import sqrt

def find_prime(num):
    """
    Given a number find that many primes
    """
    l = [2]
    count = 1
    i = 3
    while count != num:
        print i
        for j in xrange(2, int(sqrt(i+1)) + 1):
            if i % j == 0:
                break
        else:
            l.append(i)
            count += 1
        i += 2
    return l

if __name__ == '__main__':
    print find_prime(10001)
