def multi3and5(num):
    """
    Find the sum of multiples of 3 and 5 within a range a 0 to num
    """
    sum = 0
    for i in xrange(num):
        if i % 3 ==0 or i % 5 ==0:
            sum += i
    return sum

if __name__ == '__main__':
    print multi3and5(1000)

