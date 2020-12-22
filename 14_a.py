import re 
import copy

prog = []
max_mem = 0
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def bitmask(d, m):
  b = str(bin(d))
  b = b[2:]
  b = b.zfill(36)
  
  #print b
  #print m

  result = ''
  for bit in range(0, len(m)):
    if m[bit] == 'X':
      result=result+b[bit]
    if m[bit] == '0':
      result=result+'0'
    if m[bit] == '1':
      result=result+'1'
  #print result
  res = int(result, 2)
  #print res
  return res


      

with open("14_input.txt") as f:
  for line in f:
    trip = []
    match = re.search('mask = ([X01]{36})', line)
    if match:
      trip.append('mask')
      trip.append('')
      trip.append(match.group(1))
      prog.append(trip)
      continue
    match = re.search('mem\[([0-9]*)\] = ([0-9]*)', line)
    if match:
      trip.append('mem')
      trip.append(int(match.group(1)))
      trip.append(int(match.group(2)))
      prog.append(trip)
      if int(match.group(1)) > max_mem:
        max_mem = int(match.group(1))
      continue
    print "ERROR: Uninterpreted instruction"
    exit()

mem = []
for i in range(0, max_mem+1):
  mem.append(1)
  mem[i] = 0

#print prog
#print mem

for instr in prog:
  if instr[0]=='mask':
    mask = instr[2]
    continue
  if instr[0]=='mem':
    mem[instr[1]]=bitmask(instr[2], mask)

#print mem
sum = 0
for z in mem:
  sum+= z
print sum
