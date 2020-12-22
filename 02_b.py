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
  low = min[n]-1
  hi = max[n]-1
  letter = c[n]
  pword = p[n]

  count = 0
  if (pword[low] == letter):
    count = count + 1
  if (pword[hi] == letter): 
    count = count + 1 
  if count == 1:
    valid = valid + 1

print valid
