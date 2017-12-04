import math

input = 312051

def issq(n):
  sqrt = math.sqrt(n)
  if sqrt % 2 == 0: 
    return False
  if int(sqrt+0.5)**2 == n:
    return True
  else:
    return False

def total_square_count(grid_size):
  return (int(math.sqrt(grid_size)) + 1) / 2

def get_bottom_right_val(grid_size, square_number):
  return int((math.sqrt(grid_size) - (2 * square_number)) ** 2)


def get_square_side(grid_size, square_number):
  return int(math.sqrt(get_bottom_right_val(grid_size, square_number)))

def get_bottom_right_index(grid_size, square_number):
  grid_side = int(math.sqrt(grid_size))
  return (grid_side-square_number-1, grid_side-square_number-1)

def get_least_val(grid_size, square_number):
  max_val = get_bottom_right_val(grid_size, square_number)
  side = int(math.sqrt(max_val))-1
  return max_val-(4*side-1)

def adj(p, grid):
  side = len(grid)
  def left():
    if p[1] == 0:
      return None
    else:
      return (p[0], p[1]-1)

  def right():
    if p[1] == side-1:
      return None
    else:
      return (p[0], p[1]+1)

  def top():
    if p[0] == 0:
      return None
    else:
      return (p[0]-1, p[1])

  def left_top():
    if p[1] == 0  or p[0] == 0:
      return None
    else:
      return (p[0]-1, p[1]-1)

  def right_top():
    if p[0] == 0 or p[1] == side-1:
      return None
    else:
      return (p[0]-1, p[1]+1)

  def bottom():
    if p[0] == side-1:
      return None
    else:
      return (p[0]+1, p[1])

  def left_bottom():
    if p[0] == side-1 or p[1] == 0:
      return None
    else:
      return (p[0]+1, p[1]-1)

  def right_bottom():
    if p[0] == side-1 or p[1] == side-1:
      return None
    else:
      return (p[0]+1, p[1]+1)

  return (left(), right(), top(), bottom(), left_top(), left_bottom(), right_top(), right_bottom())

def fill(grid, grid_size, square_number, part1=True):
  part1_value = None
  part2_value = None

  bottom_right_val = get_bottom_right_val(grid_size, square_number)
  bottom_right_index = get_bottom_right_index(grid_size, square_number)
  side = int(math.sqrt(bottom_right_val))
  squares = total_square_count(grid_size)

  # fill right col
  x, y = bottom_right_index[0], bottom_right_index[1]
  if side == 1:
    grid[x][y] = 1
    return
  val = get_least_val(grid_size, square_number)
  for i in range(x-1, x-side, -1):
    if part1:
      grid[i][y] = val
      val += 1
      if grid[i][y] == input:
        diff = side/2-i
        part1_value = abs(diff) + squares-(square_number+1)
    else:
      ad = [grid[a[0]][a[1]] for a in adj((i,y), grid) if a is not None]
      val = sum(ad)
      grid[i][y] = val
      if val > input:
        part2_value = val
        return part2_value

  # fill top row
  x, y = i, y
  val = val
  for i in range(y-1, y-side, -1):
    if part1:
      grid[x][i] = val
      val += 1
      if grid[x][i] == input:
        diff = side/2-i
        part1_value = abs(diff) + squares-(square_number+1)
    else:
      ad = [grid[a[0]][a[1]] for a in adj((x,i), grid) if a is not None]
      val = sum(ad)
      grid[x][i] = val
      if val > input:
        part2_value = val
        return part2_value

  # fill left col
  x, y = x+1, i
  val = val
  for i in range(x, x+side-1):
    if part1:
      grid[i][y] = val
      val += 1
      if grid[i][y] == input:
        diff = side/2-i
        part1_value = abs(diff) + squares-(square_number+1)
    else:
      ad = [grid[a[0]][a[1]] for a in adj((i,y), grid) if a is not None]
      val = sum(ad)
      grid[i][y] = val
      if val > input:
        part2_value = val
        return part2_value

  # fill bottom row
  x, y = i, y+1
  val = val
  for i in range(y, y+side-1):
    if part1:
      grid[x][i] = val
      val += 1
      if grid[x][i] == input:
        diff = side/2-i
        part1_value = abs(diff) + squares-(square_number+1)
    else:
      ad = [grid[a[0]][a[1]] for a in adj((x,i), grid) if a is not None]
      val = sum(ad)
      grid[x][i] = val
      if val > input:
        part2_value = val
        return part2_value

  if part1:
    print 'part1 ', part1_value


def print_grid(grid):
  for i in grid:
    for j in i:
      print str(j) + '\t',
    print '\n'

grid_size = input
while not issq(grid_size):
  grid_size += 1

grid_side = int(math.sqrt(grid_size))
grid = [[0 for j in range(grid_side)] for i in range(grid_side)]
square_count = total_square_count(grid_size)

# part 1
fill(grid, grid_size, 0, True)

grid = [[0 for j in range(grid_side)] for i in range(grid_side)]

# part 2
square_sequence = reversed([i for i in range(square_count)])
for i in square_sequence:
  val = fill(grid, grid_size, i, False)
  if val is not None:
    print 'part2 ', val
    break