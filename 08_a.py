import re 

prog = []
visited = []
pc = 0
infinite_loop = 0
acc = 0

with open("08_input.txt") as f:
  for line in f:
    m = re.search('(.{3}) ([+-])([0-9]*)', line)
    if m:
      instruction = m.group(1)
      operand = int(m.group(2) + m.group(3))
      pair = []
      pair.append(instruction)
      pair.append(operand)
      prog.append(pair)
      visited.append(0)
    else:
      print "FAILED TO PARSE LINE: " + line


while infinite_loop == 0:
  if visited[pc]==1:
    print "LOOP!"
    print "  ACC = " + str(acc)
    infinite_loop = 1
    break
  visited[pc] = 1
  pair = prog[pc]
  ins = pair[0]
  op = pair[1]
  if ins == 'nop':
    pc = pc + 1
  elif ins == 'acc':
    acc = acc + op
    pc = pc + 1
  elif ins == 'jmp':
    pc = pc + op



    
