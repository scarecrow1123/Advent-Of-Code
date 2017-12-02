filename = "input.txt"

def result(digits,lookahead,ln):
  l = len(digits)
  sum = 0
  for idx, i in enumerate(digits):
    if i == digits[(idx+lookahead)%l]:
      sum += i
  return sum

with open(filename) as inputfile:
  digits = [int(i) for i in inputfile.read().strip('\n')]
  ln = len(digits)
  print 'part 1 ', result(digits, 1, ln)
  print 'part 2 ', result(digits, ln/2, ln)
