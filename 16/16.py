fle = open("16.txt")
contents = fle.read().splitlines()
arr = {}
rule = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

import re
for line in contents:
  numbers = re.findall("\d+", line)
  arr[numbers[0]] = {}
  tokens = line.split(" ")
  comp1 = tokens[2][0:-1]
  comp2 = tokens[4][0:-1]
  comp3 = tokens[6][0:-1]
  arr[numbers[0]][comp1] = int(numbers[1])
  arr[numbers[0]][comp2] = int(numbers[2])
  arr[numbers[0]][comp3] = int(numbers[3])
scores = {}
for key, val in arr.iteritems():
  count = 0
  for i, j in val.iteritems():
    if i == 'cats' or i == 'trees':
      if j >= rule[i]:
        count += 1
    elif i == 'pomeranians' or i == 'goldfish':
      if j <= rule[i]:
        count += 1
    else:
      if j == rule[i]:
        count += 1
  scores[key] = count
import operator
print max(scores.iteritems(), key=operator.itemgetter(1))[0]
