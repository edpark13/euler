def largest_palindrome_product(digits):
    """
    Find the producted that creates the largest palindrome when given number of

    digits
    """
    largest = 0
    for i in xrange(10**digits, 10**digits-10**(digits-1), -1):
        for j in xrange(10**digits, 10**digits-10**(digits-1), -1):
            product = i * j
            s = str(product)
            k = 0
            while True:
                if k == len(s)/2:
                    if largest < product:
                        return product, i, j
                elif s[k] == s[len(s) - k - 1]:
                    k += 1
                else:
                    break

if __name__ == '__main__':
    print largest_palindrome_product(6)
