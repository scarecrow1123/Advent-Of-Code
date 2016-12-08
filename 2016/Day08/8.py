instns = open("input.txt").read().splitlines()
display_row_size = 6
display_col_size = 50
display = [ ['.' for j in range(display_col_size)] for i in range(display_row_size)]

def rect(row, column):
  global display
  for i in range(column):
    for j in range(row):
      display[i][j] = "#"

def rotate_row(y, shift):
  temp = ['.' for i in range(display_col_size)]
  global display
  for i in range(shift):
    for j in range(display_col_size):
      temp[(j+1)%display_col_size] = display[y][j]
    for idx, i in enumerate(temp):
      display[y][idx] = i

def rotate_column(x, shift):
  temp = ['.' for i in range(display_row_size)]
  global display
  for i in range(shift):
    for j in range(display_row_size):
      temp[(j+1)%display_row_size] = display[j][x]
    for idx, i in enumerate(temp):
      display[idx][x] = i

def process_instn(instn):
  tokens = instn.split(" ")
  if instn.startswith("rect"):
    instn_params = tokens[1].split("x")
    rect(int(instn_params[0]), int(instn_params[1]))
  elif instn.startswith("rotate row"):
    row = tokens[2].split("=")[1]
    shift = tokens[4]
    rotate_row(int(row), int(shift))
  elif instn.startswith("rotate column"):
    col = tokens[2].split("=")[1]
    shift = tokens[4]
    rotate_column(int(col), int(shift))

def print_display():
  for i in display:
    print ''.join(i)

def get_lit_count():
  count = 0
  for i in display:
    count += i.count('#')
  return count

for instn in instns:
  process_instn(instn)

print get_lit_count() 
print_display()
