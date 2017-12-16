from tqdm import tqdm
a = 277
b = 349
fa = 16807
fb = 48271
d = 2147483647

def next1(n, fn, d):
  return (n*fn)%d

def next2(n, fn, d, gen):
  while True:
    val = (n*fn)%d
    if gen == 'a':
      if val % 4 == 0:
        return val
    else:
      if val % 8 == 0:
        return val
    n = val

def match(n1, n2):
  return '{:0>32b}'.format(n1)[16:] == '{:0>32b}'.format(n2)[16:]

def part1(a, b, fa, fb, d):
  c = 0
  for i in tqdm(range(40000000)):
    a = next1(a, fa, d)
    b = next1(b, fb, d)
    if match(a, b):
      c += 1
  print c

def part2(a, b, fa, fb, d):
  c = 0
  for i in tqdm(range(5000000)):
    a = next2(a, fa, d, 'a')
    b = next2(b, fb, d, 'b')
    if match(a, b):
      c += 1
  print c

#part1(a, b, fa, fb, d)
part2(a, b, fa, fb, d)
