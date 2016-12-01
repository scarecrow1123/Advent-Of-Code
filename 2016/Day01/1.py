f = open("input.txt")
lines = f.readlines()
tokens = lines[0].split(", ")
tokens[-1] = tokens[-1][0:2]
start = (0,0)
prev = (0,0)
end = (0,0)
facing_direction = "N"
visits = []

def go_next_step(move):
  global end
  global facing_direction
  direction = move[0]
  step = int(move[1:])
  x = None
  y = None
  if facing_direction == "N":
    if direction == "L":
      x = end[0] - int(step)
      y = end[1]
      facing_direction = "W"
    elif direction == "R":
      x = end[0] + int(step)
      y = end[1]
      facing_direction = "E"
  elif facing_direction == "E":
    if direction == "L":
      y = end[1] + int(step)
      x = end[0]
      facing_direction = "N"
    elif direction == "R":
      y = end[1] - int(step)
      x = end[0]
      facing_direction = "S"
  elif facing_direction == "S":
    if direction == "L":
      x = end[0] + int(step)
      y = end[1]
      facing_direction = "E"
    elif direction == "R":
      x = end[0] - int(step)
      y = end[1]
      facing_direction = "W"
  elif facing_direction == "W":
    if direction == "L":
      y = end[1] - int(step)
      x = end[0]
      facing_direction = "S"
    elif direction == "R":
      y = end[1] + int(step)
      x = end[0]
      facing_direction = "N"
  end = (x, y)   

distance2 = 0
found = False

def add_visits():
  global found
  global visits
  global distance2
  global prev
  global end
  if prev[0] > end[0]:
    for i in range(int(end[0])+1, int(prev[0]), 1):
      t = (i, end[1])
      if t in visits:
        distance2 = abs(t[0]) + abs(t[1])
        found = True
        break
      else:
        visits.append((i, end[1]))
  elif prev[0] < end[0]:
    for i in range(int(prev[0])+1, int(end[0]), 1):
      t = (i, prev[1])
      if t in visits:
        distance2 = abs(t[0]) + abs(t[1])
        found = True
        break
      else:
        visits.append((i, prev[1]))
  elif prev[1] > end[1]:
    for i in range(int(end[1])+1, int(prev[1]), 1):
      t = (end[0], i)
      if t in visits:
        distance2 = abs(t[0]) + abs(t[1])
        found = True
        break
      else:
        visits.append((end[0], i))
  elif prev[1] < end[1]:
    for i in range(int(prev[1])+1, int(end[1]), 1):
      t = (prev[0], i)
      if t in visits:
        distance2 = abs(t[0]) + abs(t[1])
        found = True
        break
      else:
        visits.append((prev[1], i))

for i in tokens:
  prev = end
  go_next_step(i)
  if not found:
    add_visits()

distance1 = abs(start[0]-end[0]) + abs(start[1]-end[1])

print distance1
print distance2
