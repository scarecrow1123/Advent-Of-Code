with open('input.txt') as inputfile:
  lines = inputfile.read().splitlines()
  child_parent = {}
  parent_children = {}
  g = {}
  costs = {}
  all_programs = set()
  for line in lines:
    tokens = line.split(" ")
    parent = tokens[0]
    children = [i.strip(',') for i in tokens[3:]]
    for child in children:
      child_parent[child] = parent
    parent_children[parent] = [[],0]
    g[parent] = []
    for i in children:
      parent_children[parent][0].append(i)
    all_programs.add(parent)
    costs[parent] = int(tokens[1][1:-1])

  root = None
  for pgm in all_programs:
    if not child_parent.has_key(pgm):
      root = pgm
      break
  print root  
  #part2
  def sum(graph, root):
    if not graph.has_key(root):
      g[root] = costs[root]
      return costs[root]
    s = 0
    for child in graph[root][0]:
      ts = sum(graph, child)
      g[root].append((child,ts))
      s += ts
    graph[root][1] = s

    return costs[root] + s
  
  sum(parent_children, root)

  def check(graph, root):
    children = graph[root]
    if len(children) > 2:
      s = {}
      for child in children:
        if not s.has_key(child[1]):
          s[child[1]] = 0
        s[child[1]] += 1
      for k,v in s.iteritems():
        if v == 1:
          for idx,child in enumerate(children):
            if k == child[1]:
              print costs[child[0]]-(k - children[(idx+1)%len(children)][1])
              if graph.has_key(child[0]):
                check(graph, child[0])
              else:
                return None
  check(g, root)
