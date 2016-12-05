keys1 = {"1": {"L": "i", "R": "2", "U": "i", "D": "4"}, "2": {"L": "1", "R": "3", "U": "i", "D": "5"}, "3": {"L": "2", "R": "i", "U": "i", "D": "6"}, "4": {"L": "i", "R": "5", "U": "1", "D": "7"}, "5": {"L": "4", "R": "6", "U": "2", "D": "8"}, "6": {"L": "5", "R": "i", "U": "3", "D": "9"}, "7": {"L": "i", "R": "8", "U": "4", "D": "i"}, "8": {"L": "7", "R": "9", "U": "5", "D": "i"}, "9": {"L": "8", "R": "i", "U": "6", "D": "i"}}
keys2 = {"1": {"L": "i", "R": "i", "U": "i", "D": "3"}, "2": {"L": "i", "R": "3", "U": "i", "D": "6"}, "3": {"L": "2", "R": "4", "U": "1", "D": "7"}, "4": {"L": "3", "R": "i", "U": "i", "D": "8"}, "5": {"L": "i", "R": "6", "U": "i", "D": "i"}, "6": {"L": "5", "R": "7", "U": "2", "D": "A"}, "7": {"L": "6", "R": "8", "U": "3", "D": "B"}, "8": {"L": "7", "R": "9", "U": "4", "D": "C"}, "9": {"L": "8", "R": "i", "U": "i", "D": "i"}, "A": {"L": "i", "R": "B", "U": "6", "D": "i"}, "B": {"L": "A", "R": "C", "U": "7", "D": "D"}, "C": {"L": "B", "R": "i", "U": "8", "D": "i"}, "D": {"L": "i", "R": "i", "U": "B", "D": "i"}}

def find_seq(keys):
  seq = []
  for line in lines:
    prev = "5"
    for move in line:
      if keys[prev][move] == "i":
        continue
      prev = keys[prev][move]
    seq.append(prev)
  return seq

print ''.join(find_seq(keys1))
print ''.join(find_seq(keys2))