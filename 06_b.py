import re 
group_answers = []
group_count = 0
group_people_count = 0

with open("06_input.txt") as f:
  this_group = ''
  for line in f:
    l = line.strip('\n')
    if l=='':
      group_count = group_count+1
      group_answers.append(''.join(sorted(this_group)))
      this_group = ''
      group_people_count=0
    else:
      if (group_people_count == 0):
        this_group=this_group+l
      else:
        new_group=''
        for x in l:
          if x in this_group:
            new_group=new_group+x
        this_group=new_group
      group_people_count=group_people_count+1
        
  if this_group != '':
    group_count = group_count+1
    group_answers.append(''.join(sorted(this_group)))

print group_answers

sum = 0
for s in group_answers:
  sum = sum + len(s)

print sum
