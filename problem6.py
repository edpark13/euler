def sum_square_difference(n):
    square = 0
    sum = 0
    for i in xrange(n):
        square += i**2
        sum += i
    return square - i

if __name__ == '__main__':
    sum_square_difference(10)
