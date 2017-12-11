filename = 'input.txt'
def f(instns, part1=True):
  copy = [i for i in instns]
  l = len(copy)
  pc = 0
  steps = 0
  while True:
    if pc >= l:
      return steps
    jump = copy[pc]
    if part1:
      copy[pc] += 1
    else:
      if jump >= 3:
        copy[pc] -= 1
      else:
        copy[pc] += 1
    pc += jump
    steps += 1

with open(filename) as inputfile:
  instns = [int(i) for i in inputfile.read().splitlines()]
  print 'part1 ', f(instns)
  print 'part2 ', f(instns, False)