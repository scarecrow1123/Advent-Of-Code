filename = 'input.txt'

with open(filename) as inputfile:
  phrase_tokens = [line.split() for line in inputfile.read().splitlines()]
  def has_dupe(tokens, part=1):
    d = {}
    for token in tokens:
      if d.has_key(''.join(sorted(token))):
        return True
      else:
        if part == 1:
          d[token] = 1
        else:
          d[''.join(sorted(token))] = 1
  c = 0
  for phrase in phrase_tokens:
    if not has_dupe(phrase):
      c += 1
  print 'part 1: ', c
  c = 0
  for phrase in phrase_tokens:
    if not has_dupe(phrase, 2):
      c += 1
  print 'part 2: ', c
