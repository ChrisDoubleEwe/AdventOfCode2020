import re 

data = []
chains = []

with open("10_input.txt") as f:
  for line in f:
    data.append(int(line.strip()))


data_sorted=sorted(data)


last = 0
this_chain = 0
for i in data_sorted:
  diff = i - last
  if diff == 1:
    this_chain += 1
  else:
    if this_chain>=2:
      chains.append(this_chain+1)
    this_chain = 0

  last = i

if this_chain>=2:
  chains.append(this_chain+1)



sum = 1
for x in chains:
  if x == 3:
    sum = sum * 2
  if x == 4:
    sum = sum * 4
  if x == 5: 
    sum = sum * 7

print sum
