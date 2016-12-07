import re
ips = open("input.txt").read().splitlines()

def reverse(string):
  return ''.join(reversed(string))

def valid_part1(string):
  for i in range(len(string)-3):
    if string[i] != string[i+1] and string[i:i+2] == reverse(string[i+2:i+4]):
      return True
  return False

count = 0
for ip in ips:
  ip_tokens = re.split("(\\[\w+\\])", ip)
  part1 = False
  valid = None
  for token in ip_tokens:
    if token.startswith("["):
      if valid_part1(token[1:-1]):
        part1 = False
        break
    if valid_part1(token):
      part1 = True
  if part1:
    count += 1

print count
