ip = open("3.txt").read()
res = []
robo = []
santa = []
ln = len(ip)
start = (0,0)
res.append(start)
robo.append(start)
santa.append(start)
cur = start
santa_cur = start
robo_cur = start
for i in xrange(ln):
  if ip[i] == '>':
    if i % 2 == 0:
      santa_cur = (santa_cur[0], santa_cur[1]+1)
    elif i % 2 != 0:
      robo_cur = (robo_cur[0], robo_cur[1]+1)
    cur = (cur[0], cur[1]+1)
  elif ip[i] == '<':
    if i % 2 == 0:
      santa_cur = (santa_cur[0], santa_cur[1]-1)
    elif i % 2 != 0:
      robo_cur = (robo_cur[0], robo_cur[1]-1)
    cur = (cur[0], cur[1]-1)
  elif ip[i] == '^':
    if i % 2 == 0:
      santa_cur = (santa_cur[0]+1, santa_cur[1])
    elif i % 2 != 0:
      robo_cur = (robo_cur[0]+1, robo_cur[1])
    cur = (cur[0]+1, cur[1])
  elif ip[i] == 'v':
    if i % 2 == 0:
      santa_cur = (santa_cur[0]-1, santa_cur[1])
    elif i % 2 != 0:
      robo_cur = (robo_cur[0]-1, robo_cur[1])
    cur = (cur[0]-1, cur[1])
  if cur not in res:
    res.append(cur)
  if santa_cur not in santa and santa_cur not in robo and i % 2 == 0:
    santa.append(santa_cur)
  if robo_cur not in robo and robo_cur not in santa and i % 2 != 0:
    robo.append(robo_cur)
print len(res)
print len(santa)+len(robo)-1
