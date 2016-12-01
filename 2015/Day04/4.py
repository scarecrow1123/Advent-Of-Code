import md5
ip = "bgvyzdsv"
i = 0
while True:
  tempip = ip
  tempip += str(i)
  temp = md5.new(tempip).hexdigest()
  if temp.startswith("000000"):
    break
  else:
    i += 1
  continue
print i
