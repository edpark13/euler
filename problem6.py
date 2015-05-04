def sum_square_difference(n):
    square = 0
    sum = 0
    for i in xrange(n + 1):
        square += i**2
        sum += i
    return sum**2 - square

if __name__ == '__main__':
    print sum_square_difference(100)
