from tqdm import tqdm
with open('input.txt') as inputfile:
  text = inputfile.read()
  moves = text.split(',')
  pgms = [chr(97+i) for i in range(16)]

  def spin(lst, n):
    return lst[0-n:]+lst[:0-n]
  
  def exchange(lst, a, b):
    new_lst = [i for i in lst]
    new_lst[a], new_lst[b] = new_lst[b], new_lst[a]
    return new_lst

  def partner(lst, a, b):
    ap = lst.index(a)
    bp = lst.index(b)
    new_lst = [i for i in lst]
    new_lst[ap], new_lst[bp] = new_lst[bp], new_lst[ap]
    return new_lst

  def dance(moves, pgms):
    l = [i for i in pgms]
    for move in moves:
      if move[0] == 's':
        l = spin(l, int(move[1:]))
      elif move[0] == 'x':
        tokens = move[1:].split('/')
        l = exchange(l, int(tokens[0]), int(tokens[1]))
      elif move[0] == 'p':
        tokens = move[1:].split('/')
        l = partner(l, tokens[0], tokens[1])
    return l

  l = dance(moves, pgms)
  print ''.join(l)
  original = ''.join(l)
  
  i = 0
  while True:
    i += 1
    l = dance(moves, l)
    if ''.join(l) == original:
      break

  times = (1000000000 % i)-1
  l = original
  for i in range(times):
    l = dance(moves, l)
  print ''.join(l)
