import re 
group_answers = []
group_count = 0

with open("06_input.txt") as f:
  this_group = ''
  for line in f:
    l = line.strip('\n')
    if l=='':
      group_count = group_count+1
      group_answers.append(''.join(sorted(set(this_group))))
      this_group = ''
    else:
      this_group=this_group+l
  if this_group != '':
    group_count = group_count+1
    group_answers.append(''.join(sorted(set(this_group))))

print group_answers

sum = 0
for s in group_answers:
  sum = sum + len(s)

print sum
