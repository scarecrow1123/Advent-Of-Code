ip = """Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.
"""

import re
import operator
lines = ip.splitlines()
arr = {}
clock = 2504 
curr = {}
for line in lines:
  tokens = line.split(" ")
  numbers = re.findall("\d+", line)
  arr[tokens[0]] = {}
  curr[tokens[0]] = {}
  arr[tokens[0]]["speed"] =  int(numbers[0])
  arr[tokens[0]]["go"] = int(numbers[1])
  arr[tokens[0]]["rest"] = int(numbers[2])
  curr[tokens[0]]["dist"] = 0
  curr[tokens[0]]["rest"] = int(numbers[2])
  curr[tokens[0]]["state"] = "go"
  curr[tokens[0]]["go"] = int(numbers[1])
  curr[tokens[0]]["points"] = 0
for time in range(1, clock):
  for i in curr:
    if curr[i]["state"] == "go":
      curr[i]["dist"] += arr[i]["speed"]
      curr[i]["go"] -= 1
    if curr[i]["state"] == "rest":
      curr[i]["rest"] -= 1
    if curr[i]["go"] == 0:
      curr[i]["go"] = arr[i]["go"]
      curr[i]["state"] = "rest"
    if curr[i]["rest"] == 0:
      curr[i]["rest"] = 0
      curr[i]["state"] = "go"
      curr[i]["rest"] = arr[i]["rest"]
  dists = [] 
  for i in curr:
    dists.append(curr[i]["dist"])
  j = max(dists)
  for i in curr:
    if curr[i]["dist"] == j:
      curr[i]["points"] += 1
p = []
for i in curr:
  p.append(curr[i]["points"])
print max(p)

