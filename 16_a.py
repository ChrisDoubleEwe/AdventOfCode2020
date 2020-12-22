import re 

rules = []
my_ticket = []
tickets = []
dest = 0
min = 999
max = 0
with open("16_input.txt") as f:
  for l in f:
    line=l.strip('\n')
    print line
    if line == '':
      continue
    if line == 'your ticket:':
      dest += 1
      continue
    if line == 'nearby tickets:':
      dest += 1
      continue
    if dest == 0:
      match = re.search('([^:]*): ([0-9]*)-([0-9]*) or ([0-9]*)-([0-9]*)', line)
      label = match.group(1)
      a_lower = int(match.group(2))
      a_upper = int(match.group(3))
      b_lower = int(match.group(4))
      b_upper = int(match.group(5))
      rule = []
      rule.append(label)
      rule.append(a_lower)
      rule.append(a_upper)
      rule.append(b_lower)
      rule.append(b_upper)
      rules.append(rule)
      if a_lower < min:
        min = a_lower
      if b_upper > max:
        max = b_upper

    if dest == 1:
      fields=line.split(',')
      for f in fields:
        my_ticket.append(int(f))
    if dest == 2:
      field = []
      fields=line.split(',')
      for f in fields:
        field.append(int(f))
      tickets.append(field)

print "Rules================"
print rules
print "\nMy ticket================"
print my_ticket
print "\nTickets================"
print tickets

print min
print max

valid = []

for r in rules:
  for i in range(r[1], r[2]+1):
    if i not in valid:
      valid.append(i)
  for i in range(r[3], r[4]+1):
    if i not in valid:
      valid.append(i)

print valid

sum = 0
for t in tickets:
  for v in t:
    if v not in valid:
      print "INVALID: " + str(v)
      sum += v

print '=========='
print sum


