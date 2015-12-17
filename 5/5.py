ip = open("5.txt").read()
from sets import Set
double = Set(["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx", "yy", "zz"])
follow = Set(["ab", "cd", "xy", "pq"])
lines = ip.splitlines()
nice = 0
for line in lines:
  vowelcount = 0
  ln = len(line)
  tempdouble = []
  tempfollow = []
  for i in xrange(ln):
    if line[i] == 'a' or line[i] == 'e' or line[i] == 'i' or line[i] == 'o' or line[i] == 'u':
      vowelcount += 1
    if i != ln-1:
      tempdouble.append(line[i] + line[i+1])
      tempfollow.append(line[i] + line[i+1])
  tempdoubleset = Set(tempdouble)
  tempfollowset = Set(tempfollow)
  tempdoubleset.intersection_update(double)
  tempfollowset.intersection_update(follow)
  doublelen = len(tempdoubleset)
  followlen = len(tempfollowset)
  if vowelcount >= 3 and doublelen >= 1 and followlen == 0:
    nice += 1
print nice
