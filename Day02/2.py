ip = open("2.txt").read()
lines = ip.splitlines()
area = 0
length = 0
for line in lines:
  dim = line.split("x")
  temparea = 2*int(dim[0])*int(dim[1]) + 2*int(dim[1])*int(dim[2]) + 2*int(dim[0])*int(dim[2])
  temparea += min([int(dim[0])*int(dim[1]), int(dim[1])*int(dim[2]), int(dim[0])*int(dim[2])])
  area += temparea
  length += int(dim[0]) * int(dim[1]) * int(dim[2])
  temp = [int(dim[0]), int(dim[1]), int(dim[2])]
  length += 2* min(temp)
  temp.remove(min(temp))
  length += 2* min(temp)

print length


