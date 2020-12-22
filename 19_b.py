from printf import printf
import copy
import re 

eight_recursions = 0
eleven_recursions = 0

rules = {}
messages = []
with open("19_input_b.txt") as f:
  for l in f:
    if ':' in l:
      if '"' in l:
        # 4: "a"
        match = re.search('([0-9]*): "([a-z])"', l)
        rules[int(match.group(1))] = match.group(2)
        continue
      if '|' in l:
        # 1: 2 3 | 3 2
        match = re.search('([0-9]*): ([0-9 |]*)', l)
        rules[int(match.group(1))] = ' (?: ' + match.group(2) + ' ) '
        continue
      else:
        # 0: 4 1 5
        match = re.search('([0-9]*): ([0-9 ]*)', l)
        rules[int(match.group(1))] = match.group(2)
        continue
    else:
      if l.strip() != '':
        messages.append(l.strip())

def insert_position(position, list1, list2):
  return list1[:position] + list2 + list1[position:]


def hasNumbers(inputString):
  return bool(re.search(r'\d', inputString))

print rules



my_rule = ' ' + rules[0] + ' ' 
print my_rule
while hasNumbers(my_rule):
  for i in rules.keys():
    print rules[i]
    match = re.search(' 8 ', my_rule)
    if match:
      eight_recursions+=1
    match = re.search(' 11 ', my_rule)
    if match:
      eleven_recursions+=1
    if eight_recursions > 2000:
      my_rule = my_rule.replace(' 8 ', ' no_more_recursion ' )
    if eleven_recursions > 2000:
      my_rule = my_rule.replace(' 11 ', ' no_more_recursion ' )


      
    my_rule = my_rule.replace(' '+str(i)+' ', ' ' + rules[i] + ' ' )
    print my_rule



my_rule = my_rule.replace(' ', '')
my_rule = '^'+my_rule+'$'
print my_rule

print "CHECKING MESSAGES"
print "================="

num = 0
for x in messages:
  print x 
  match = re.search(my_rule, x)
  if match:
    print "  matches!"
    num+=1

print "TOTAL MATCHES"
print "============="
print num
