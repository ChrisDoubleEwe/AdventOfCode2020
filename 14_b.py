import re 
import copy

prog = []
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def bitmask(addr, d, m):
  global mem

  b = str(bin(addr))
  b = b[2:]
  b = b.zfill(36)
  
  result = ''
  for bit in range(0, len(m)):
    if m[bit] == 'X':
      result=result+'X'
    if m[bit] == '0':
      result=result+b[bit]
    if m[bit] == '1':
      result=result+'1'
  all_addresses = []
  all_addresses.append(result)
  iter = 0
  while 'X' in all_addresses[0]:
    iter += 1
    this_addr = all_addresses.pop(0)
    idx = this_addr.find('X')
    this_addr1=this_addr
    this_addr2=this_addr
    s = this_addr1[:idx] + '0' + this_addr1[idx + 1:]
    this_addr1 = s
    s = this_addr2[:idx] + '1' + this_addr2[idx + 1:]
    this_addr2 = s
    all_addresses.append(this_addr1)
    all_addresses.append(this_addr2)
 
  for x in all_addresses:
    dec_addr = int(x, 2)
    mem[dec_addr] = d

      

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
      continue
    print "ERROR: Uninterpreted instruction"
    exit()

mem = {}


tot = len(prog)
iteration = 0
for instr in prog:
  iteration += 1
  if instr[0]=='mask':
    mask = instr[2]
    continue
  if instr[0]=='mem':
    bitmask(instr[1], instr[2], mask)


sum = 0
for key, value in mem.items():
  sum += value

print sum
