def largestPrime(num):
    """
    Find the largest prime factor of a number
    """
    i = 2

    while i * i < num:
        while num%i == 0:
            num = num / i
        i += 1

    return num

if __name__ == '__main__':
    print largestPrime(600851475143)
