def evenFibNum():
    l = [1, 2]
    i = 2
    while True:
        num = l[-2] + l[-1]
        if num < 4000000:
            l.append(num)
        else:
            break
        i += 1
    sum = 0
    for j in l:
        if j % 2 ==0:
            print j
            sum += j
    return sum

if __name__ == '__main__':
    print evenFibNum()
