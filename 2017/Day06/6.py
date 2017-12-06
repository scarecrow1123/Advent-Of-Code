from collections import OrderedDict

with open('input.txt') as inputfile:
  blocks = [int(i) for i in inputfile.read().strip('\n').split("\t")]
  def max_n_index(lst):
    mx = 0
    mx_id = 0
    for idx, i in enumerate(lst):
      if i > mx:
        mx = i
        mx_id = idx
    return (mx,mx_id)

  config_set = OrderedDict()

  i = 0
  config_set[tuple(blocks)] = True
  while True:
    mx, mx_id = max_n_index(blocks)
    j = (mx_id+1)% 16
    while True:
      if j == mx_id or blocks[mx_id] <= 0:
        break
      blocks[j] += 1
      blocks[mx_id] -= 1
      j = (j+1) % 16
    t = tuple(blocks)
    if config_set.has_key(t):
      configs = config_set.keys()
      l = len(configs)
      print 'part 2 ', l-configs.index(t)
      i+=1
      break
    config_set[t] = True
    i += 1
  print 'part 1 ',i
