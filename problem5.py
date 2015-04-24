def smallest_multiple(n):
    i = 1
    while True:
        for j in xrange(n,9999999999,n):
            if i % j != 0:
                break
            return i
        i += 1

if __name__ == '__main__':
    print smallest_multiple(10)
