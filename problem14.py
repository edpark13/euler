def collatz_seq(n):
  length = 0
  while n > 1:
    length += 1
    if n % 2 == 0:
      n /= 2
    else:
      n = 3 * n + 1
  return length + 1

def longest_collatz_seq(n):
  max = [0, 0]
  for i in xrange(1, n):
    length = collatz_seq(i)
    if length > max[0]:
      max[0] = length
      max[1] = i
  print str(max[1]) + " with length " + str(max[0])

if __name__ == '__main__':
  # print collatz_seq(13)
  longest_collatz_seq(1000000)
