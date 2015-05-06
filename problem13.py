def large_sum():
    """
    From a file get the sum of all the digits that are seperated by lines
    """
    f = open("13number.txt", 'r')
    sum = 0
    for line in f.readlines():
        sum += int(line)
    return sum

if __name__ == '__main__':
    print str(large_sum())
    print str(large_sum())[0:10] # print only the first 10 digits
