from Queue import *

def adj(graph, node):
  ne = (node[0]-1,node[1]+1)
  se = (node[0]+1,node[1]+1)
  nw = (node[0]-1,node[1]-1)
  sw = (node[0]+1,node[1]-1)
  n = (node[0]-2,node[1])
  s = (node[0]+2,node[1])
  def foo(d):
    return d
  return (foo(ne), foo(se),
          foo(nw), foo(sw),
          foo(n), foo(s))

def get_dir(parent, child):
  if parent[1] == child[1] and parent[0]-1 == child[0]:
    return 'n'
  if parent[1] == child[1] and parent[0]+1 == child[0]:
    return 's'
  if parent[0]-1 == child[0] and parent[1]+1 == child[1]:
    return 'ne'
  if parent[0]+1 == child[0] and parent[1]+1 == child[1]:
    return 'se'
  if parent[0]-1 == child[0] and parent[1]-1 == child[1]:
    return 'nw'
  if parent[0]+1 == child[0] and parent[1]-1 == child[1]:
    return 'sw'

def bfs_distance(graph, root, target, explored):
  q = Queue()
  seen = {}
  distance = {}
  distance2 = {}
  q.put(root)
  seen[root] = True
  explored_len = len(explored)
  explored_seen = 1
  while q.qsize() != 0:
    v = q.get(False)
    for child in adj(graph, v):
      if child is None:
        continue
      if not seen.has_key(child) or not seen[child]:
        if not distance.has_key(child):
          distance[child] = 0
        if not distance.has_key(v):
          distance[v] = 0
        distance[child] = distance[v] + 1
        seen[child] = True
        if child in explored:
          explored_seen += 1
          distance2[child] = distance[child]
        if child == target:
          print 'part1 ', distance[child]
        if explored_seen == explored_len:
          break
        q.put(child)
  print 'part2 ', max(distance2.values())

def step(graph, direction, curr):
  next = None
  if direction == 'ne':
    next = (curr[0]-1, curr[1]+1)
  elif direction == 'se':
    next = (curr[0]+1, curr[1]+1)
  elif direction == 'nw':
    next = (curr[0]-1, curr[1]-1)
  elif direction == 'sw':
    next = (curr[0]+1, curr[1]-1)
  elif direction == 'n':
    next = (curr[0]-2, curr[1])
  elif direction == 's':
    next = (curr[0]+2, curr[1])

  graph[next[0]][next[1]] = 1
  return next

def print_grid(grid):
  for i in grid:
    for j in i:
      print str(j) + '\t',
    print '\n'

with open('input.txt') as inputfile:
  text = inputfile.read().strip("\n")
  directions = text.split(",")
  l = len(directions)
  grid = [[0 for j in range(10001)] for i in range(10001)]
  curr = (5000,5000)
  grid[curr[0]][curr[1]] = 1
  print 'Total directions ', l
  explored = set()
  explored.add(curr)

  for idx,dir in enumerate(directions):
    curr = step(grid, dir, curr)  
    explored.add(curr)
  bfs_distance(grid, (5000, 5000), curr, explored)
