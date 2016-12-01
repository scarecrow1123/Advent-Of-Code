ip = "hepxxzaa" 

def red_prev(password, pos):
  cur_token = chr(ord(password[pos]))
  temp = cur_token
  if temp == 'z':
    temp = 'a'
  else:
    temp = chr(ord(temp)+1)
  if pos == 0:
    password = password[0] + temp + password[1:]
  else:
   password = password[0:pos] + temp + password[pos+1:]
  if cur_token == 'z':
    password = red_prev(password, pos-1)
  return password

double = {"aa": "aaa", "bb": "bbb", "cc": "ccc", "dd": "ddd", "ee": "eee", "ff": "fff", "gg": "ggg", "hh": "hhh", "ii": "iii", "jj": "jjj", "kk": "lll", "mm": "mmm", "nn": "nnn", "oo": "ooo", "pp": "ppp", "qq": "qqq", "rr": "rrr", "ss": "sss", "tt": "ttt", "uu": "uuu", "vv": "vvv", "xx": "xxx", "yy": "yyy", "zz": "zzz"}

def validate(password):
  rule1 = False
  rule2 = False
  rule3 = False
  for i in range(1, len(password)-1):
    if ord(password[i]) - ord(password[i-1]) == 1 and ord(password[i+1]) - ord(password[i]) == 1:
      rule1 = True
  if 'i' not in password or 'o' not in password or 'l' not in password:
    rule2 = True
  contains = []
  for key, val in double.iteritems():
    if key in password and val not in password and key not in contains:
      contains.append(key)
  if len(contains) >= 2:
    rule3 = True
  return rule1 and rule2 and rule3
  
def incr(password):
  i = 0
  while not validate(password):
    cur = chr(ord(password[-1]))
    temp = cur
    if temp == 'z':
      temp = 'a'
    else:
      temp = chr(ord(temp)+1)
    password = password[0:-1] + temp
    if cur == 'z':
      password = red_prev(password, -2)
    i +=1
    print password
  return password

print incr(ip)
