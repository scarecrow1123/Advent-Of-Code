with open('input.txt') as inputfile:
  registers = {}

  def tokens(instn):
    return instn.split(" ")

  condition = {
        "==" : lambda x,y: x == y,
        "<" : lambda x,y: x < y,
        ">" : lambda x,y: x > y,
        "!=": lambda x,y: x != y,
        ">=": lambda x,y: x >= y,
        "<=": lambda x,y: x <= y
      }

  operation = {
        "inc": lambda x,y: x + y,
        "dec": lambda x,y: x - y
      }


  def parse(tokens):
    reg, op, op_val, reg_cond, cond, cond_val = tokens[0], tokens[1], int(tokens[2]), tokens[4], tokens[5], int(tokens[6])
    
    if not registers.has_key(reg):
      registers[reg] = 0
    if not registers.has_key(reg_cond):
      registers[reg_cond] = 0

    if condition[cond](registers[reg_cond], cond_val):
      result = operation[op](registers[reg], op_val)
      registers[reg] = result
      return result

  instns = inputfile.read().splitlines()
  mx2 = 0
  for instn in instns:
    toks = tokens(instn)
    val = parse(toks)
    if val > mx2:
      mx2 = val
  
  mx1 = 0
  for reg, val in registers.iteritems():
    if val > mx1:
      mx1 = val

  print mx1
  print mx2
