with open('input.txt') as inputfile:
  text = inputfile.read().strip('\n')
  lengths = [int(i) for i in text.split(',')]
  elements = [i for i in range(256)]
  
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

  part1 = run(elements, lengths, 1)
  print part1[0] * part1[1]

  lengths = [ord(i) for i in text]
  lengths.extend([17, 31, 73, 47, 23])
  part2 = run(elements, lengths, 64)
  part2 = hash(part2)
  hashstr = []
  for i in part2:
    h = tohex(i)
    hashstr.append(h)
  print ''.join(hashstr)
