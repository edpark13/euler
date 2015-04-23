def evenFibNum():
    """
    Get the sum of only even Fibonacci that are less than 4000000
    """
    l = [1, 2]
    i = 2
    sum = 0
    while True:
        num = l[-2] + l[-1]
        if num < 4000000:
            l.append(num)
            if num % 2 == 0:
                sum += num
        else:
            break
        i += 1
    return sum

if __name__ == '__main__':
    print evenFibNum()
