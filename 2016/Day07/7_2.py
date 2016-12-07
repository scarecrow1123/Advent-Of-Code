import re
ips = open("input.txt").read().splitlines()

def valid(string):
  valid = []
  for i in range(len(string)-2):
    if string[i] == string[i+2] and string[i] != string[i+1]:
      valid.append(string[i:i+3])
  if len(valid) > 0:
    return valid
  else:
    return None

count = 0
for ip in ips:
  ip_tokens = re.split("(\\[\w+\\])", ip)
  valid_hypernets = []
  valid_supernets = []
  for token in ip_tokens:
    if token.startswith("["):
      val = valid(token[1:-1])
      if val is not None:
        valid_hypernets.extend(val)
    else:
      val = valid(token)
      if val is not None:
        valid_supernets.extend(val)
  for i in valid_supernets:
    temp = i[1] + i[0] + i[1]
    if temp in valid_hypernets:
      count += 1
      break

print count
