from math import sqrt

def special_pythagorean_triplet(num):
    """
    Given a number return a product that is sum of the 
    special pythagorean triplet
    """
    for a in xrange(1, 1000):
        for b in xrange(1, 1000):
            c = sqrt(a**2 + b**2)
            if a + b + c == num:
                return a * b * c

if __name__ == '__main__':
    print special_pythagorean_triplet(1000)
