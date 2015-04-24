def largestPrime(n):
    """
    Find the largest prime factor of a number
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            print i
            n //= i
    return n

if __name__ == '__main__':
    print largestPrime(100)
