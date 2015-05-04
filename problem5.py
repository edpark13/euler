def smallest_multiple(n):
    """
    Find the smallest number that is divisible by number 2 to n
    """
    l = [(2, 2)]
    i = 2
    for k in xrange(2, n + 1):
        if i % k > 0:
            for j in xrange(2, n + 1):
                if i * j % k == 0:
                    i *= j
                    l.append((k, j))
                    break
    print l
    return i

if __name__ == '__main__':
    print smallest_multiple(10)
