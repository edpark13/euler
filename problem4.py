def largest_palindrome_product(digits):
    """
    Find the producted that creates the largest palindrome when given number of

    digits
    """
    for i in xrange(10**digits, 10**digits-10**(digits-1), -1):
        for j in xrange(10**digits, 10**digits-10**(digits-1), -1):
            product = i * j
            print product, i, j
            s = str(product)
            if s == s[::-1]:
                return product, i, j

if __name__ == '__main__':
    print largest_palindrome_product(3)
