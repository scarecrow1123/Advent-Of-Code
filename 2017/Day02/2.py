import re

filename = 'input.txt'

with open(filename) as inputfile:
  lines = inputfile.read().splitlines()
  sheet = [[int(i) for i in re.split("\s", line)] for line in lines]
  print 'part 1: ', reduce(lambda x,y: x+(max(y)-min(y)), sheet, 0)

  def foo(y):
    for idx, i in enumerate(y):
      l = len(y)
      for idy, j in enumerate(y):
        if idx == idy:
          continue
        if i %j == 0:
          return i/j

  print 'part 2: ', reduce(lambda x,y : x+foo(y), sheet, 0)
