ip = open("6.txt").read()
i, j = 1000, 1000
arr = []
for x in xrange(i):
  temp = []
  for y in xrange(j):
    temp.append(0)
  arr.append(temp)
count = 0
for x in xrange(i):
  for y in xrange(j):
    count += 1
lines = ip.splitlines()
for line in lines:
  temp = ""
  command = ""
  if line.find("turn on") == 0:
    temp = line.strip("turn on")
    command = "on"
  elif line.find("turn off") == 0:
    temp = line.strip("turn off")
    command = "off"
  elif line.find("toggle") == 0:
    temp = line.strip("toggle")
    command = "tog"
  tokens = temp.split(" through ")
  start = tokens[0].split(",")
  end = tokens[1].split(",")
  startx, starty = int(start[0]), int(start[1])
  endx, endy = int(end[0]), int(end[1])
  for l in range(startx, endx+1):
    for m in range(starty, endy+1):
      if command == "on":
        arr[l][m] += 1
      elif command == "off":
	if arr[l][m] != 0:
	  arr[l][m] -= 1
      elif command == "tog":
        arr[l][m] += 2
lit = 0
for x in xrange(i):
  for y in xrange(j):
    lit += arr[x][y]
print lit
