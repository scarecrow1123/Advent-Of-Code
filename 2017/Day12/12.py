from Queue import *

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

with open('input.txt') as inputfile:
  lines = inputfile.read().splitlines()

  pgms = {}
  for line in lines:
    tokens = line.split(" ")
    pgm = int(tokens[0])
    pgms[pgm] = []
    direct_connections = [int(i.strip(','))for i in tokens[2:]]
    pgms[pgm].extend(direct_connections)

  total = len(pgms.keys())
  seen = set(bfs(pgms, 0))
  print len(seen)

  pgm_list = []
  for pgm in pgms.keys():
    if pgm not in seen:
      pgm_list.append(pgm)

  i = 1
  while True:
    if len(seen) == total:
      break
    p = pgm_list.pop()
    new_seen = bfs(pgms, p)
    for j in new_seen:
      seen.add(j)
      if j in pgm_list:
        pgm_list.remove(j)

    for pgm in pgms.keys():
      if pgm not in seen and pgm not in pgm_list:
        pgm_list.append(pgm)
    i += 1
  print i
    
