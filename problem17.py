import inflect

def number_letter_counts(num):
  words = inflect.engine().number_to_words(num)
  print words
  return len(words.replace(" ", "").replace("-", ""))

if __name__ == '__main__':
  sum = 0
  for i in xrange(1, 1001):
    sum += number_letter_counts(i)
  print "answer is " + str(sum)
