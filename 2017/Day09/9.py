with open('input.txt') as inputfile:
  text = inputfile.read().strip(' ').strip('\n')
  container = []
  garbage = False
  skip = False
  score = 0
  garbage_count = 0
  for idx, i in enumerate(text):
    if skip:
      skip = False
      continue

    if i == '!':
      skip = True
      continue

    if garbage and not skip and i == '>':
      garbage = False
      continue

    if garbage and not skip:
      garbage_count += 1
      continue

    if i == '<':
      garbage = True
      continue

    if i == '{':
      container.append(i)
      continue

    if i == '}' and container[-1] == '{':
      container.pop()
      score += len(container)+1
      continue
  print score
  print garbage_count
