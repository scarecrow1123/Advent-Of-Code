def reverse(elements, start, length):
  temp = [i for i in elements]
  templen = len(temp)
  if length > templen:
    return elements
  s = start
  e = (start+length-1)%templen

  for i in range(length/2):
    t = temp[s]
    temp[s] = temp[e]
    temp[e] = t

    s = (s+1)%templen
    e = (e-1)%templen

  return temp

def run(elements, lengths, times):
  curr = 0
  skip = 0
  elements_len = len(elements)
  for i in range(times):
    for length in lengths:
      elements = reverse(elements, curr, length)
      curr = (curr + length + skip)%elements_len
      skip += 1
  return elements

def hash(elements):
  dense = []
  for i in range(0, len(elements), 16):
    d = elements[i]
    for j in range(1,16):
      d ^= elements[i+j]
    dense.append(d)
  return dense

hex_map = {
    0:'0',1:'1',2:'2',3:'3',
    4:'4',5:'5',6:'6',7:'7',
    8:'8',9:'9',10:'a',11:'b',
    12:'c',13:'d',14:'e',15:'f'
    }

def tohex(number):
  hex = []
  while True:
    quotient = number / 16
    remainder = number % 16
    number = quotient
    hex.append(hex_map[remainder])
    if quotient == 0:
      break
  hex = [i for i in reversed(hex)]
  return ''.join(hex).zfill(2)

def part1():
  part1 = run(elements, lengths, 1)
  print part1[0] * part1[1]

def get_hash(text):
  elements = [i for i in range(256)]
  lengths = [ord(i) for i in text]
  lengths.extend([17, 31, 73, 47, 23])
  hinter = run(elements, lengths, 64)
  hinter = hash(hinter)
  hashstr = []
  for i in hinter:
    h = tohex(i)
    hashstr.append(h)
  return ''.join(hashstr)

hex_binary = {
    '0': '0000', '1': '0001', '2': '0010',
    '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'a': '1010', 'b': '1011',
    'c': '1100', 'd': '1101', 'e': '1110',
    'f': '1111'
    }

text = "nbysizxe"
grid = ['#' for j in range(128) for i in range(128)]
rows = [text+'-'+str(i) for i in range(128)]
row_binary = []

for row in rows:
  hashval = get_hash(row)
  binary = []
  for i in hashval:
    binary.append(hex_binary[i])
  binary = ''.join(binary)
  row_binary.append(binary)

squares = 0
for row in row_binary:
  squares += row.count('1')
print squares


def bfs(graph, root):
  q = Queue()
  seen = {}
  distance = {}
  q.put(root)
  seen[root] = True
  while q.qsize() != 0:
    v = q.get(False)
    for child in graph[v]:
      if child is None:
        continue
      if not seen.has_key(child) or not seen[child]:
        if not distance.has_key(child):
          distance[child] = 0
        if not distance.has_key(v):
          distance[v] = 0
        distance[child] = distance[v] + 1
        seen[child] = True
        q.put(child)
  return seen.keys()
