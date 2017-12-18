with open('input.txt') as inputfile:
  instns = inputfile.read().splitlines()
  n_instns = len(instns)

  registers = {0: {chr(i):0 for i in range(97,97+26)},
               1: {chr(i):0 for i in range(97,97+26)}
              }
  registers[1]['p'] = 1

  sounds = {0: [], 1: []}
  pgm_ctr = {0:0, 1:0}

  def snd(freq, pgm):
    global sounds, pgm_ctr
    if registers[pgm].has_key(freq):
      if pgm == 0:
        sounds[1].append(registers[pgm][freq])
      else:
        sounds[0].append(registers[pgm][freq])
    else:
      if pgm == 0:
        sounds[1].append(int(freq))
      else:
        sounds[0].append(int(freq))

  def set(x, y, pgm):
    global registers, pgm_ctr
    if registers[pgm].has_key(y):
      registers[pgm][x] = registers[pgm][y]
    else:
      registers[pgm][x] = int(y)

  def add(x, y, pgm):
    global registers, pgm_ctr
    if registers[pgm].has_key(y):
      registers[pgm][x] += registers[pgm][y]
    else:
      registers[pgm][x] += int(y)

  def mul(x, y, pgm):
    global registers, pgm_ctr
    if registers[pgm].has_key(y):
      registers[pgm][x] *= registers[pgm][y]
    else:
      registers[pgm][x] *= int(y)
  
  def mod(x, y, pgm):
    global registers, pgm_ctr
    if registers[pgm].has_key(y):
      registers[pgm][x] %= registers[pgm][y]
    else:
      registers[pgm][x] %= int(y)

  def rcv(x, pgm):
    global sounds, pgm_ctr
    if len(sounds[pgm]) == 0:
      return None
    msg = sounds[pgm].pop(0)
    registers[pgm][x] = msg
    return msg
  
  def jgz(x, y, pgm):
    global registers
    global pgm_ctr
    if registers[pgm].has_key(x):
      if registers[pgm][x] > 0:
        if registers[pgm].has_key(y):
          return registers[pgm][y]
        else:
          return int(y)
      else:
        return 1
    elif int(x) > 0:
      if registers[pgm].has_key(y):
        return registers[pgm][y]
      else:
        return int(y)

  def isnum(st):
    try:
      int(st)
      return True
    except ValueError:
      return False 

  def run():
    cmds = {
      "set": lambda x,y,pgm: set(x,y,pgm),
      "add": lambda x,y,pgm: add(x,y,pgm),
      "mul": lambda x,y,pgm: mul(x,y,pgm),
      "mod": lambda x,y,pgm: mod(x,y,pgm),
      "snd": lambda x,dummy,pgm: snd(x,pgm),
      "rcv": lambda x,dummy,pgm: rcv(x,pgm),
      "jgz": lambda x,y,pgm: jgz(x,y,pgm)
      }

    tokenize = lambda x: x.split(" ")
    parse = lambda x: [x[0]] + [int(i) if isnum(i) else i for i in x[1:]] + [None]
    extract = lambda x: parse(tokenize(x))

    wait_0 = False
    wait_1 = True
    stop_0 = False
    stop_1 = False
    send_1 = 0

    while True:
      print pgm_ctr[0], pgm_ctr[1]
      #print instns[pgm_ctr[0]], instns[pgm_ctr[1]]
      if (wait_0 and wait_1) or (stop_0 and stop_1):
        break

      if not wait_0 and not stop_0:
        t = extract(instns[pgm_ctr[0]])
        (cmd, x), y = t[0:2], t[2:][0]

        if cmd == 'rcv' and len(sounds[0]) == 0:
          wait_0 = True
          continue

        ret = cmds[cmd](x,y,0)

        if cmd == 'snd':
          wait_1 = False

        if cmd == 'jgz':
          pgm_ctr[0] += ret
        else:
          pgm_ctr[0] += 1

      if not wait_1 and not stop_1:
        t = extract(instns[pgm_ctr[1]])
        (cmd, x), y = t[0:2], t[2:][0]

        if cmd == 'rcv' and len(sounds[1]) == 0:
          wait_1 = True
          continue

        ret = cmds[cmd](x,y,1)

        if cmd == 'snd':
          wait_0 = False
          send_1 += 1

        if cmd == 'jgz':
          pgm_ctr[1] += ret
        else:
          pgm_ctr[1] += 1

      if pgm_ctr[0] >= n_instns or pgm_ctr[0] < 0:
        stop_0 = True
      if pgm_ctr[1] >= n_instns or pgm_ctr[1] < 0:
        stop_1 = True

    print send_1
  run()
