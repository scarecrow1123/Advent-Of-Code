ip = """43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38
"""

arr = [int(line) for line in ip.splitlines()]
from itertools import combinations
from sets import Set
count = 0
min_containers = []
length = 99999999999999999
for i in range(1, len(arr)+1):
  combs = combinations(arr, i)
  for idx, j in enumerate(combs):
    if sum(j) == 150:
      count += 1
      ln = len(j) 
      if ln <= length:
        min_containers.append(j)
        length = ln
print count        
print len(min_containers)

