lines = open("9.txt").read().splitlines()
arr = ["AlphaCentauri", "Snowdin", "Tambi", "Faerun", "Norrath", "Straylight", "Tristram", "Arbre"]
import itertools
perms = [x for x in itertools.permutations(arr)]
arr1 = {}
for line in lines:
  tokens = line.split(" ")
  arr1[tokens[0]] = {}
  arr1[tokens[2]] = {}
for line in lines:
  tokens = line.split(" ")
  arr1[tokens[0]][tokens[2]] = int(tokens[-1])
  arr1[tokens[2]][tokens[0]] = int(tokens[-1])
dists = []
for i in perms:
  dist = 0
  for idx, j in enumerate(i):
    if idx == len(i)-1:
      break
    dist += arr1[i[idx]][i[idx+1]]
  dists.append(dist)
print max(dists)
