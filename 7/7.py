import re
ip = open("7.txt").read()
lines = ip.splitlines()
arr = {}

def do_op(lp, rp, op):
  if op == 'RSHIFT':
    return lp >> rp
  elif op == 'LSHIFT':
    return lp << rp
  elif op == 'OR':
    return lp | rp
  elif op == 'AND':
    return lp & rp
def init():
  for line in lines:
      lst = re.split(r' -> ', line)
      var = lst[-1]
      arr[var] = {}
      ltokens = lst[0].split(" ")
      arr[var]["value"] = ""
      if len(ltokens) == 1:
        arr[var]["value"] = ltokens[0]
        try:
          temp = int(ltokens[0])
          with_values.append(var)
        except:
          pass
      if len(ltokens) == 2 and ltokens[0] == 'NOT':
        arr[var]["not"] = ltokens[1]
      if len(ltokens) == 3:
        arr[var]["lparen"] = ltokens[0]
        arr[var]["rparen"] = ltokens[2]
        arr[var]["op"] = ltokens[1]
def solve():
  with_values = []  
  ln_values = len(with_values)
  ln_keys = len(arr.keys())
  i = 0
  while ln_values != ln_keys:
    i += 1
    for key, val in arr.iteritems():
      for k, v in val.iteritems():
        if v in with_values:
          arr[key][k] = arr[v]["value"]
      curr_keys = val.keys()
      temp_with_values = []
      if not str(val["value"]).isdigit():
        if "not" in curr_keys and str(val["not"]).isdigit():
          arr[key]["value"] = ~(int(val["not"])) % 65536
      if "lparen" in curr_keys and "rparen" in curr_keys and str(val["lparen"]).isdigit() and str(val["rparen"]).isdigit():
        arr[key]["value"] = do_op(int(val["lparen"]), int(val["rparen"]), val["op"])

      for key,val in arr.iteritems():
        if str(val["value"]).isdigit():
          temp_with_values.append(key)
      with_values = list(temp_with_values)
      ln_values = len(with_values)
init()
solve()
a_value = arr["a"]["value"]
init()
arr["b"] = {"value": a_value}
solve()
print arr["a"]["value"]
