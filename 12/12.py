count = 0
def foo(f, tp):
  global count
  if tp is "dict":
    if f.has_key("red") or "red" in f.values():
      return 0
    for k, v in f.iteritems():
      if k == 'red':
        continue
      if type(v) is dict:
        foo(v, "dict")
      elif type(v) is list:
        foo(v, "list")
      elif v == 'red':
        continue
      elif type(v) is int:
        count = count + v
  elif tp is "list":
    for x in f:
      if type(x) is int:
        count = count + x
      elif type(x) is list:
        foo(x, "list")
      elif type(x) is dict:
        foo(x, "dict")
  return count
f = open("12.txt")
rd = f.read()
import json
st = json.loads(rd)
foo(st, "dict")
print count
