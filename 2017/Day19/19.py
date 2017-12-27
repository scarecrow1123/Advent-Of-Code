import sys
with open('input.txt') as inputfile:
  maze = [[j for j in i] for i in inputfile.read().splitlines()]
  xsize = len(maze)
  ysize = len(maze[0])

  def step(maze, current_position):
    x,y = current_position
  
  def print_maze(maze):
    for i in maze:
      print i

  def get_chr(pos, maze):
    return maze[pos[0]][pos[1]]

  def get_next(pos, dir, maze):
    def next():
      if dir == 'up':
        return (pos[0]-1, pos[1])
      elif dir == 'down':
        return (pos[0]+1, pos[1])
      elif dir == 'left':
        return (pos[0], pos[1]-1)
      elif dir == 'right':
        return (pos[0], pos[1]+1)
    nxt = next()
    if nxt[0] < 0 or nxt[0] >= xsize:
      return None
    if nxt[1] < 0 or nxt[1] >= ysize:
      return None
    if get_chr(nxt, maze) == ' ':
      return None
    return nxt

  opposite = {
        'up': 'down',
        'down': 'up',
        'left': 'right',
        'right': 'left'
      }

  def get_dir(chr, pos, curr_dir, maze):
    if chr == '+':
      for i in ['up', 'down', 'left', 'right']:
        if i == opposite[curr_dir]:
          continue
        nxt = get_next(pos, i, maze)
        if nxt is None:
          continue
        if get_chr(nxt, maze) != ' ':
          return i
    else:
      return curr_dir

  def explore(maze):
    pos = (0, maze[0].index('|'))
    char_at_pos = get_chr(pos, maze)
    dirn = get_dir(char_at_pos, pos, 'down', maze)
    st = ''
    steps = 1
    while True:
      nxt = get_next(pos, dirn, maze)
      if nxt is None:
        break
      char_at_pos = get_chr(nxt, maze)
      dirn = get_dir(char_at_pos, nxt, dirn, maze)
      if char_at_pos not in ['-', '|', '+']:
        st += char_at_pos
      pos = nxt
      steps += 1

    return (st, steps)
  part1, part2 = explore(maze)
  print 'part1 ', part1
  print 'part2 ', part2
