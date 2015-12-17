import re
ip = open("13.txt").read()
lines = ip.splitlines()
arr = {"Alice": {"me": 0}, "Bob": {"me": 0}, "Carol": {"me": 0}, "David": {"me": 0}, "Eric": {"me": 0}, "Frank": {"me": 0}, "George": {"me": 0}, "Mallory": {"me": 0}, "me": {"Alice": 0, "Bob": 0, "Carol": 0, "David": 0, "Eric": 0, "Frank": 0, "George": 0, "Mallory": 0}}
for line in lines:
	tokens = line.split(" ")
	point = re.findall("\d+", line)[0]
	if line.find("gain") != -1:
		point = int(point)
	elif line.find("lose") != -1:
		point = 0 - int(point)
	arr[tokens[0]][tokens[-1].strip(".")] = point

lst = ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory", "me"]
from itertools import permutations
perm = permutations(lst)
arrangements = []
max_happ = 0
for idx, j in enumerate(perm):
	arrangements.append(j)
	happiness = 0
	for i in j:
		left = j[(j.index(i)-1)%9]
		right = j[(j.index(i)+1)%9]
		happiness += arr[i][left] + arr[i][right]
	if happiness > max_happ:
		max_happ = happiness
print max_happ
