ip = open("3.txt").read()
res = []
ln = len(ip)
start = (0,0)
res.append(start)
cur = start
for i in xrange(ln):
  if ip[i] == '>':
    cur = (cur[0], cur[1]+1)
  elif ip[i] == '<':
    cur = (cur[0], cur[1]-1)
  elif ip[i] == '^':
    cur = (cur[0]+1, cur[1])
  elif ip[i] == 'v':
    cur = (cur[0]-1, cur[1])
  try:
    res.index(cur)
  except:
    res.append(cur)
  continue
print len(res)


