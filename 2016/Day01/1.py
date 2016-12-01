f = open("input.txt")
lines = f.readlines()
tokens = lines[0].split(", ")
tokens[-1] = tokens[-1][0:2]
start = (0,0)
end = (0,0)
facing_direction = "N"

def go_next_step(move):
  global end
  global facing_direction
  direction = move[0]
  step = move[1]
  if direction == "L":
    if facing_direction == "N":
      t = end[0] - int(step)
      end = (t, end[1])
      facing_direction = "W"
    elif facing_direction == "E":
      t = end[1] + int(step)
      end = (end[0], t)
      facing_direction = "N"
    elif facing_direction == "S":
      t = end[0] + int(step)
      end = (t, end[1])
      facing_direction = "E"
    elif facing_direction == "W":
      t = end[1] - int(step)
      end = (end[0], t)
      facing_direction = "S"
  elif direction == "R":
    if facing_direction == "N":
      t = end[0] + int(step)
      end = (t, end[1])
      facing_direction = "E"
    elif facing_direction == "E":
      t = end[1] - int(step)
      end = (end[0], t)
      facing_direction = "S"
    elif facing_direction == "S":
      t = end[0] - int(step)
      end = (t, end[1])
      facing_direction = "W"
    elif facing_direction == "W":
      t = end[1] + int(step)
      end = (end[0], t)
      facing_direction = "N"
for i in tokens:
  go_next_step(i)

distance = abs(start[0]-end[0]) + abs(start[1]-end[1])
print distance
