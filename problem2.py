def evenFibNum():
    l = []
    for i in xrange(10):
        try:
            l.append(i + l[-1])
        except IndexError:
            l.append(i)

    return l

if __name__ == '__main__':
    print evenFibNum()
