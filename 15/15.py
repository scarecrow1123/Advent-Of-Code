ip="""Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
"""
lines = ip.splitlines()
arr = {}
for line in lines:
  tokens = line.split(" ")
  name = tokens[0][0:-1]
  arr[name] = {}
  arr[name]["capacity"] = int(tokens[2].strip(","))
  arr[name]["durability"] = int(tokens[4].strip(","))
  arr[name]["flavor"] = int(tokens[6].strip(","))
  arr[name]["texture"] = int(tokens[8].strip(","))
  arr[name]["calories"] = int(tokens[10].strip(","))
scores = []
for i in range(1, 101):
  for j in range(1, 101):
    for k in range(1, 101):
      for l in range(1, 101):
        if i+j+k+l != 100:
          continue
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0
        tup = (i,j,k,l)
        count = 0
        for m in arr:
          capacity += arr[m]["capacity"] * tup[count]
          durability += arr[m]["durability"] * tup[count]
          flavor += arr[m]["flavor"] * tup[count]
          texture += arr[m]["texture"] * tup[count]
          calories += arr[m]["calories"] * tup[count]
          count += 1
        if capacity < 0:
          capacity = 0;
        if durability < 0:
          durability = 0
        if flavor < 0:
          flavor = 0
        if texture < 0:
          texture = 0
        if calories < 0:
          calories = 0
        if calories == 500:
          scores.append(capacity * durability * flavor * texture)

print (max(scores))        


