ip = open("1_1.txt").read()
count = 0
ln = len(ip)
for i in xrange(ln):
  if ip[i] == '(':
    count = count + 1
  elif ip[i] == ')':
    count = count - 1
  if count == -1:
    print i + 1
    break




