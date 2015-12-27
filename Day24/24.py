lines = open("24.txt").read().splitlines()
weights = [int(x) for x in lines]
count = len(weights)
import itertools
group_weight = sum(weights) / 4
min_len = 999999999
min_qe = 99999999999999999999
for i in range(1, count+1):
  group1_combos = itertools.combinations(weights, i)
  for g1c in group1_combos:
    if sum(g1c) == group_weight:
      if len(g1c) < min_len:
        min_len = len(g1c)
        qe = reduce(lambda x,y: x*y, g1c)
        if qe < min_qe:
          min_qe = qe
  if i > 4:
    break
print min_qe
