import re 

prog = []
visited = []
pc = 0
infinite_loop = 0
terminated = 0
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

orig_prog = list(prog)

for change_line in range(0, len(prog)):
  prog = list(orig_prog)
  infinite_loop = 0
  terminated = 0
  acc = 0
  pc = 0
  for i in range(0, len(prog)):
    visited[i]=0

  pair = prog[change_line]
  new_pair = []
  if pair[0] == 'nop':
    new_pair.append('jmp')
  elif pair[0] == 'jmp':
    new_pair.append('nop')
  else:
    new_pair.append(pair[0])
  new_pair.append(pair[1])
  prog[change_line] = new_pair

  
  while infinite_loop == 0:
    if pc == len(prog):
      print "TERMINATED!"
      print "  ACC = " + str(acc)
      terminated = 1
      break
    if visited[pc]==1:
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

  if (terminated == 1):
    break


    
