def evenFibNum():
    l = []
    i = 0
    while True:
        i += 1
        try:
            num = i + l[-1]
            print num
            if num < 4000000:
                l.append(num)
            else:
                break
        except IndexError:
            l.append(i)
    sum = 0
    for j in l:
        sum += j
    return sum

if __name__ == '__main__':
    print evenFibNum()
