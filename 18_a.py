from printf import printf
import copy
import re 

# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
def evaluate(s):
  while ' ' in s:
    if '(' in s:
      match = re.search('\(([0-9 \+\*]*)\)', s)
      sub_clause = match.group(1)
      result = evaluate(sub_clause)
      new_expr = s.replace("(" + sub_clause + ")", str(result))
      s = new_expr
    else:
      x = s.split(' ')
      res = 0
      while len(x) > 1:
        op1 = int(x.pop(0))
        op  = x.pop(0)
        op2 = int(x[0])
        if op == '+':
          res = op1 + op2
        if op == '*':
          res = op1 * op2
        x[0] = res
      return x[0]
  return evaluate(s)
    
with open("18_input.txt") as f:
  tot = 0
  for l in f:
    result = evaluate(l.strip('\n'))
    print "RESULT: " + str(result)
    tot += result

print "\n\nTOTAL: " + str(tot)
