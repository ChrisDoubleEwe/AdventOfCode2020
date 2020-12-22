import re 

preamble = 25
data = []
proc = []

with open("09_input.txt") as f:
  for line in f:
    data.append(int(line.strip()))

index = 0
for i in range(0, preamble):
  proc.append(data[i])
  index = index + 1

valid = 1
while valid == 1:
  this_value = data[index]
  pair_found = 0
  for x in proc:
    if this_value - x == x:
      continue
    if (this_value - x) in proc:
      pair_found = 1
      break
  if pair_found == 1:
    proc.append(data[index])
    proc.pop(0)
    index=index+1 
  else:
    valid = 0
  
print str(this_value)

for start in range (0, len(data)):
  sum = 0
  index = 0
  while (sum < this_value) and (start + index <= len(data)):
    sum = sum + data[start+index]
    index = index + 1
  if sum == this_value:
    min = data[start]
    max = data[start]
    for i in range (start, start+index):
      if data[i] < min:
        min = data[i]
      if data[i] > max:
        max = data[i]
    result = max + min
    print "Max: " + str(max) + " ; Min: " + str(min)
    print result
    break
 
