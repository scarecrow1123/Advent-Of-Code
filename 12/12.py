ip = open("12.txt").read()
import re
arr = re.findall(r'[-\d]+', ip)
s = 0
for i in arr:
	s += int(i)

def foo(f, tp, count):
	if tp is "dict":
		if f.has_key("red") or "red" in f.values():
			return
		for k, v in d.iteritems():
			if k == 'red':
				continue
			if type(v) is dict:
				count += foo(v, "dict", count)
			elif type(v) is list:
				count+= foo(v, "list", count)
			elif v == 'red':
				continue
			else:
				count += v
	elif tp is "list":
		for x in f:
			if type(x) is int:
				count += x
	return count
print foo(ip, "dict", -1)
