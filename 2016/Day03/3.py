import sys,re
from itertools import combinations
f = open("input.txt")

def valid_triangle(sides):
  for combo in combinations(sides, 2):
    diff = None
    try:
      diff_set = set(sides).difference(set(combo))
      diff_val = diff_set.pop()
    except:
      continue
    valid = sum(combo) > int(diff_val)
    if not valid:
      return False
  return True

def find_possible_triangles(all_sides):
  possible = 0
  ln = len(all_sides)
  for i in range(0, ln+1, 3):
    sides = (all_sides[i:i+3])
    if len(sides) == 0:
      continue
    if valid_triangle((all_sides[i:i+3])):
      possible += 1
  return possible

inp = f.read()
lines1 = inp.splitlines()
all_sides1 = [int(i) for i in re.split("\s+", inp.strip())]
print find_possible_triangles(all_sides1)
all_sides2 = []
t = [0,3,6,1,4,7,2,5,8]
for i in range(0, len(all_sides1)-8, 9):
  for j in t:
    all_sides2.append(all_sides1[i+j])
print find_possible_triangles(all_sides2)
