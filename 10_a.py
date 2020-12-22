import re 

data = []
chains = []

with open("10_input.txt") as f:
  for line in f:
    data.append(int(line.strip()))


data_sorted=sorted(data)


sum_1 = 0
sum_2 = 0
sum_3 = 0
last = 0
print data_sorted
for i in data_sorted:
  diff = i - last
  print diff
  if diff == 1:
    sum_1 += 1
  if diff == 2:
    sum_2 += 1
  if diff == 3:
    sum_3 += 1
  last = i

sum_3 += 1
print "----------"
print sum_1
print sum_2
print sum_3


answer = sum_1 * sum_3
print "ANSWER = " + str(answer)
