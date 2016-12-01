lines = open("23.txt").read().splitlines()
ref_table = {}
ctr = 1

def compute(instn):
  global ctr
  if instn["instn"] == "jmp":
    ctr += instn["offset"]
    return
  if instn["instn"] == "inc":
    regs[instn["register"]] += 1
  elif instn["instn"] == "hlf":
    regs[instn["register"]] /= 2
  elif instn["instn"] == "tpl":
    regs[instn["register"]] *= 3
  elif instn["instn"] == "jie" and regs[instn["register"]] % 2 == 0:
    ctr += instn["offset"]
    return
  elif instn["instn"] == "jio" and regs[instn["register"]] == 1:
    ctr += instn["offset"]
    return
  ctr += 1

def init():  
  global ref_table
  for idx, line in enumerate(lines):
    tokens = line.split(" ")
    instn_map = {}
    instn_map["instn"] = tokens[0]
    if tokens[0] == "jmp":
      instn_map["register"] = ""
      instn_map["offset"] = int(tokens[1])
    else:
      instn_map["register"] = tokens[1].split(",")[0]
    if len(tokens) > 2:
      instn_map["offset"] = int(tokens[2])
    ref_table[idx+1] = instn_map

def go():
  while True:
    compute(ref_table[ctr])
    if ctr not in instn_numbers:
      break
init()
instn_numbers = ref_table.keys()
regs = {"a": 0, "b": 0}
go()
print regs["b"]
ctr = 1
regs = {"a": 1, "b": 0}
go()
print regs["b"] 
