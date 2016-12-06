lines = open("input.txt").read().splitlines()
column_count = len(lines[0])
column_char_count = { i:{} for i in range(column_count) }
for line in lines:
  for idx, char in enumerate(line):
    if not column_char_count[idx].has_key(char):
      column_char_count[idx][char] = 0
    column_char_count[idx][char] += 1

part1 = []
part2 = []

for i in column_char_count.iteritems():
  mx_count = 0
  mx_char = None 
  mn_count = 9999999999999999
  mn_char = None
  for j in i[1].iteritems():
    if j[1] > mx_count:
      mx_count = j[1]
      mx_char = j[0]
    if j[1] < mn_count:
      mn_count = j[1]
      mn_char = j[0]
  part1.append(mx_char)
  part2.append(mn_char)
print ''.join(part1)
print ''.join(part2)
