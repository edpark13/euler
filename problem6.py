def sum_square_difference(n):
    """
    Find the difference between the sum of the numbers 1 to n squared and the
    numbers 1 to n squared added
    """
    square = 0
    sum = 0
    for i in xrange(1, n + 1):
        square += i**2
        sum += i
    return sum**2 - square

if __name__ == '__main__':
    print sum_square_difference(100)
