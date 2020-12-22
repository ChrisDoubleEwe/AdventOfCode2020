import re 

content = []
with open("02_input.txt") as f:
  for line in f:
    content.append(line.strip('\n'))

min = []
max = []
c = []
p = []

for x in content:
  match = re.search('([0-9]*)-([0-9]*) ([a-z]): ([a-zA-Z]*)', x)
  min.append(int(match.group(1)))
  max.append(int(match.group(2)))
  c.append(str(match.group(3)))
  p.append(str(match.group(4)))

valid = 0
for n in range(0, len(p)):
  low = min[n]
  hi = max[n]
  letter = c[n]
  pword = p[n]
  count = pword.count(letter) 
  if (count >= low) and (count <= hi):
    valid = valid + 1

print valid
