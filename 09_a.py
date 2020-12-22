import re 

preamble = 25
data = []
proc = []

with open("09_input.txt") as f:
  for line in f:
    data.append(int(line.strip()))

print data

index = 0
for i in range(0, preamble):
  proc.append(data[i])
  index = index + 1

print proc
print data[index]

valid = 1
while valid == 1:
  this_value = data[index]
  pair_found = 0
  for x in proc:
    if this_value - x == x:
      continue
    if (this_value - x) in proc:
      print "  pair found: " + str(this_value) + " = " + str(x) + " + " + str(this_value - x)
      pair_found = 1
      break
  if pair_found == 1:
    proc.append(data[index])
    proc.pop(0)
    index=index+1 
  else:
    print "INVALID VALUE " + str(this_value)
    valid = 0
  

