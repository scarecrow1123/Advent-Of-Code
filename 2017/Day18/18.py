with open('input.txt') as inputfile:
  instns = inputfile.read().splitlines()
  n_instns = len(instns)

  registers = {chr(i):0 for i in range(97,97+26)}
  sounds = []
  pgm_ctr = 0

  def snd(freq):
    global sounds, pgm_ctr
    pgm_ctr += 1
    if registers.has_key(freq):
      sounds.append(registers[freq])
    else:
      sounds.append(int(freq))

  def set(x, y):
    global registers, pgm_ctr
    pgm_ctr += 1
    if registers.has_key(y):
      registers[x] = registers[y]
    else:
      registers[x] = int(y)

  def add(x, y):
    global registers, pgm_ctr
    pgm_ctr += 1
    if registers.has_key(y):
      registers[x] += registers[y]
    else:
      registers[x] += int(y)

  def mul(x, y):
    global registers, pgm_ctr
    pgm_ctr += 1
    if registers.has_key(y):
      registers[x] *= registers[y]
    else:
      registers[x] *= int(y)
  
  def mod(x, y):
    global registers, pgm_ctr
    pgm_ctr += 1
    if registers.has_key(y):
      registers[x] %= registers[y]
    else:
      registers[x] %= int(y)

  def rcv(x):
    global sounds, pgm_ctr
    pgm_ctr += 1
    if registers.has_key(x):
      if registers[x] != 0:
        return sounds.pop()
    elif int(x) != 0:
      return sounds.pop()
    return None
  
  def jgz(x, y):
    global registers
    global pgm_ctr
    if registers.has_key(x):
      if registers[x] > 0:
        if registers.has_key(y):
          pgm_ctr += registers[y]
        else:
          pgm_ctr += int(y)
      else:
        pgm_ctr += 1
    elif int(x) > 0:
      if registers.has_key(y):
        pgm_ctr += registers[y]
      else:
        pgm_ctr += int(y)

  def run():
    while True:
      if pgm_ctr >= n_instns:
        break
      if pgm_ctr < 0:
        break
      instn = instns[pgm_ctr]
      tokens = instn.split(' ')
      command = tokens[0]
      x = tokens[1]
      if len(tokens) > 2:
        y = tokens[2]
      if command == 'set':
        set(x,y)
      elif command == 'add':
        add(x,y)
      elif command == 'mul':
        mul(x,y)
      elif command == 'mod':
        mod(x,y)
      elif command == 'snd':
        snd(x)
      elif command == 'rcv':
        recovered = rcv(x)
        print recovered
        break
      elif command == 'jgz':
        jgz(x,y)
  run()
  
