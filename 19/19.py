ip = open("19.txt").read()
import re
def replace_n(word, to_replace, replacement, n):
  start = 0
  replacelen = len(to_replace)
  i = 1
  idx = 0
  ret_list = []
  while True:
    idx = word.find(to_replace, start)
    if idx == 0 and n == 1:
      ret_list.append(replacement)
      ret_list.append(word[replacelen:])
      break
    if idx == -1:
      break
    if i == n:
      ret_list.append(word[0:idx])
      ret_list.append(replacement)
      ret_list.append(word[idx+replacelen:])
      break
    i += 1
    start = idx + replacelen
  return ''.join(ret_list)
  
arr = {}
lines = ip.splitlines()
molecule = ""
for line in lines:
  tokens = re.split(" => ", line)
  if len(tokens) == 1:
    molecule = line
  else:
    arr[tokens[0]] = []
for line in lines:
  tokens = re.split(" => ", line)
  if len(tokens) > 1:
    arr[tokens[0]].append(tokens[1])
replacements = []
def part1():
  for key, val in arr.iteritems():
    occurrence_count = len(re.findall(key, molecule))
    for j in range(1, occurrence_count+1):
      for i in val:
        replacements.append(replace_n(molecule, key, i, j))
from sets import Set
part1()
print len(Set(replacements))
