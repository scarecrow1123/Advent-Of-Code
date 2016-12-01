ip = open("18.txt").read()
lines = ip.splitlines()
arr = []
for line in lines:
  arr.append([i for i in line])
arrlen = len (arr)
x = 0
for x in xrange(100):
  x += 1
  to_on = []
  to_off = []
  for idx, i in enumerate(arr):
    for idy, j in enumerate(i):
      if (idx == 0 and idy == 0) or (idx == 0 and idy == len(i)-1) or (idx == len(arr)-1 and idy == 0) or (idx == len(arr)-1 and idy == len(i)-1):
        arr[idx][idy] = '#'
        continue
      on_neighbours = 0
      ilen = len(i)
      if idx > 0 and arr[idx-1][idy] == '#':
        on_neighbours += 1
      if idx < ilen-1 and arr[idx+1][idy] == '#':
        on_neighbours += 1
      if idy > 0 and arr[idx][idy-1] == '#':
        on_neighbours += 1
      if idy < arrlen-1 and arr[idx][idy+1] == '#':
        on_neighbours += 1
      if idx > 0 and idy > 0 and arr[idx-1][idy-1] == '#':
        on_neighbours += 1
      if idx < ilen-1 and idy < arrlen-1 and arr[idx+1][idy+1] == '#':
        on_neighbours += 1
      if idx > 0 and idy < arrlen - 1 and arr[idx-1][idy+1] == '#':
        on_neighbours += 1
      if idx < arrlen - 1 and idy > 0 and arr[idx+1][idy-1] == '#':
        on_neighbours += 1
      if j == '#' and (on_neighbours == 2 or on_neighbours == 3):
        to_on.append((idx, idy))
      elif j == '#':
        to_off.append((idx, idy))
      if j == '.' and (on_neighbours == 3):
        to_on.append((idx, idy))
  for i in to_on:
    arr[i[0]][i[1]] = '#'
  for i in to_off:
    arr[i[0]][i[1]] = '.'
final_count = 0      
for idx, i in enumerate(arr):
  for idy, j in enumerate(i):
    if j == '#':
      final_count += 1
print final_count      
