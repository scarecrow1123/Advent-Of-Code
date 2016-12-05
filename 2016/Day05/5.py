import md5
ip = "reyedfim"
part1 = []
part2 = [0 for i in range(8)]
part2_indices = {i: False for i in range(8)}
found_part1 = 0
found_part2 = 0
def find_next_char(idx):
  global password
  global ip
  global found_part1
  global found_part2
  while True:
    hashinput = ip+str(idx)
    hexdigest = md5.new(hashinput).hexdigest()
    if hexdigest.startswith("00000"):
      if not found_part1 == 8:
        part1.append(hexdigest[5])
        found_part1 += 1
      if not found_part2 == 8:
        try:
          if part2_indices.has_key(int(hexdigest[5])) and not part2_indices[int(hexdigest[5])]:
            part2[int(hexdigest[5])] = hexdigest[6]
          else:
            return idx
        except ValueError:
          return idx
        except IndexError:
          return idx
        found_part2 += 1
        part2_indices[int(hexdigest[5])] = True
      return idx
    idx += 1

current_idx = -1
while not(found_part1 == 8 and found_part2 == 8):
  current_idx = find_next_char(current_idx+1)
print ''.join(part1)
print ''.join(part2)
