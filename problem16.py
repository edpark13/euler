def power_digit_sum(num, power):
  n = num ** power
  digits = len(str(n))
  sum = 0
  for i in xrange(digits):
    sum += int(str(n)[i])
  return sum

def pow2sum(num, power):
  L = list(str(num ** power))
  return sum([int(i) for i in L])

if __name__ == '__main__':
  print power_digit_sum(2, 1000)
  print pow2sum(2, 1000)
