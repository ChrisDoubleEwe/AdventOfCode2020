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


valid = []

rule_values=[]
for r in rules:
  this_rule_values = []
  for i in range(r[1], r[2]+1):
    this_rule_values.append(i)
    if i not in valid:
      valid.append(i)
  for i in range(r[3], r[4]+1):
    this_rule_values.append(i)
    if i not in valid:
      valid.append(i)
  rule_values.append(this_rule_values)

valid_tickets = []
for t in tickets:
  isvalid = 1
  for v in t:
    if v not in valid:
      isvalid = 0
  if isvalid == 1:
    valid_tickets.append(t)

print "\n\n\nValid tickets================"
print valid_tickets

print rule_values


field_matches = []
for r in rules:
  field_matches.append(-1)

print field_matches

all_field_values = []
for i in range(0, len(rules)):
  this_field_values = []
  for t in valid_tickets:
    this_field_values.append(t[i])
  all_field_values.append(this_field_values)
print all_field_values



matching_rules = []
for i in range(0, len(rules)):
  this_matching_rules = []
  z=all_field_values[i]
  for r in range(0, len(rules)):
    match_rule = 1
    for x in z:
      if x not in rule_values[r]:
        match_rule = 0
    if match_rule == 1:
      print "Field: " + str(i) + " matches rule " + str(r)
      this_matching_rules.append(r)
  matching_rules.append(this_matching_rules)

print matching_rules 

done = 0
while done == 0:
  done = 1
  for r in matching_rules:
    print r
    if len(r) == 1:
      for i in range(0, len(matching_rules)):
        if len(matching_rules[i]) > 1:
          if r[0] in matching_rules[i]:
            matching_rules[i].remove(r[0])
            done = 0

print matching_rules

result = 1
for i in range(0, len(matching_rules)):
  label = rules[matching_rules[i][0]][0]
  print 'Field ' + str(i) + " is rule " + label
  if 'departure' in label:
    print "  MATCH!!!" 
    val = my_ticket[i]
    result = result * val


print "=========RESULT==========="
print result
 
