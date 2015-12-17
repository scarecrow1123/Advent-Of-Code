ip = "1321131112 "

arr = []
prev = ip[0] 
count = 0
j = 0
while j in xrange(50):
	arr = []
	for i, token in enumerate(ip):
		if prev == token:
			count += 1
		else:
			arr.append((str(count), prev))
			count = 1 
		prev = token
	st = []
	for x in arr:
		st.append(x[0])
		st.append(x[1])
	stt = "".join(st) + " "
	print len(stt)
	print "\n"
	j += 1
	prev = stt[0]
	ip = stt
	count = 0
