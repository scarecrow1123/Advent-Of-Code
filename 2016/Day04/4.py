import re

data = open("input.txt").read().splitlines()
rooms = [(lambda x: (x[0][0:-1], x[1], x[2][1:-1]))(re.split("(\d+)", i)) for i in data]

def get_char_frequency(string):
  freq = {}
  for i in string:
    if freq.has_key(i):
      freq[i] += 1
    else:
      freq[i] = 0
  return freq

def is_room_real(name, checksum):
  name = ''.join(name.split("-"))
  name_freq = get_char_frequency(name)
  prev_count = 0
  prev_char = None
  for i in checksum:
    try:
      curr_count = name_freq[i]
    except KeyError:
      return False
    if curr_count > prev_count and prev_char is not None:
      return False
    if curr_count == prev_count and prev_char is not None and prev_char > i:
      return False
    prev_char = i
    prev_count = curr_count
  return True 
  
def decrypt(name, sectorid):
  decrypted_name = []
  for i in name:
    if i == "-":
      decrypted_name.append(" ")
      continue
    for j in range(int(sectorid)):
      i = chr(ord('a') + ((ord(i)-ord('a')+1)%26))
    decrypted_name.append(i)
  return ''.join(decrypted_name)

total = 0
decrypted = False
for room in rooms:
  if is_room_real(room[0], room[2]):
    total += int(room[1])
    if not decrypted:
      decrypted_name = decrypt(room[0], room[1])
      if decrypted_name in "northpole object storage":
        print "part 2 : " + str(room[1])
        decrypted = True
      
print "part 1 : " + str(total)
