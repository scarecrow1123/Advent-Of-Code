from collections import OrderedDict

with open('input.txt') as inputfile:
  lines = inputfile.read().splitlines()
  depth_range = {}
  mx = 0
  for line in lines:
    tokens = line.split(": ")
    depth = int(tokens[0])
    r = int(tokens[1])
    depth_range[depth] = r
    if depth > mx:
      mx = depth

  t = [i for i in range(mx+1)]
  
  for idx,i in enumerate(t):
    if depth_range.has_key(i):
      t[idx] = depth_range[i]
    else:
      t[idx] = None
  

  scanner_pos = [[0,1] for i in range(mx+1)]
  lscanner = len(scanner_pos)
  packet_pos = 0

  def step_scanner():
    global scanner_pos

    for idx,i in enumerate(scanner_pos):
      if t[idx] is not None:
        if scanner_pos[idx][0] == t[idx]-1:
          scanner_pos[idx][1] = -1
        elif scanner_pos[idx][0] == 0:
          scanner_pos[idx][1] = 1
        scanner_pos[idx][0]  = (scanner_pos[idx][0] + scanner_pos[idx][1])%t[idx]

  tlen = len(t)
  s = 0
  time = 0
  while True:
    if time >= len(t):
      break
    if t[time] is not None:
      if scanner_pos[packet_pos][0] == 0:
        s += time*t[time]
    packet_pos += 1
    step_scanner()
    time += 1
  print s
  
  delay = 0
  while True:
    delay += 1
    s = 0
    time = 0
    packet_pos = 0
    while True:
      if packet_pos >= tlen:
        break
      if time >= delay:
        if t[packet_pos] is not None:
          if scanner_pos[packet_pos][0] == 0:
            s += 1
            break
        packet_pos += 1
      step_scanner()
      time += 1
    if s == 0:
      print '**'
      with open('out.txt', 'w') as outf:
        outf.write(delay)
      print delay
      break
