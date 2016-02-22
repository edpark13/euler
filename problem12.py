def num_of_divisors(num):
  if num == 0:
    return 0
  divisors = 1
  count = 0
  while num % 2 == 0:
    count += 1
    num = num / 2
  divisors = divisors * (count + 1)

  p = 3
  while num != 1:
    count = 0
    while num % p == 0:
      count += 1
      num = num / p
    divisors = divisors * (count + 1)
    p += 2

  return divisors

def find_triangular_num(max):
  n = 1
  sum = 0
  while num_of_divisors(sum) < max:
    sum += n
    n += 1
  print sum

if __name__ == '__main__':
  find_triangular_num(500)
  # print num_of_divisors(0)
