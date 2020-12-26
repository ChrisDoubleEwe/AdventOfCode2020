from printf import printf
import copy
import re 
import math

input = '389125467'
input = '219347865'

max_cup = 0
cups = []
for i in input:
  cups.append(int(i))
  if int(i) > max_cup:
    max_cup = int(i)

print cups
current_cup = 0

moves = 100

this_move = 0
while this_move < moves:
  this_move += 1
  print "-- move " + str(this_move) + " --"

  printf('cups: ')
  for i in range(0, len(cups)):
    if i == current_cup:
      printf('('+str(cups[i])+') ')
    else:
      printf(str(cups[i])+' ')
  print ''

  # Get current cup
  current_cup_val = cups[current_cup]

  # Pick up next 3 cups clockwise 
  pop_cups = []
  pop_cup_pos = current_cup+1 
  for i in range(0, 3):
    if pop_cup_pos < len(cups): 
      cup = cups.pop(pop_cup_pos)
      pop_cups.append(cup)
    else:
      pop_cup_pos = 0
      cup = cups.pop(pop_cup_pos)
      pop_cups.append(cup)
  print 'pick up: ' + str(pop_cups)
  
  # Work out destination cup 
  current_cup = cups.index(current_cup_val)
  try_dest = cups[current_cup]
  if try_dest > 1:
    try_dest -= 1
  else:
    try_dest = max_cup

  while try_dest not in cups:
    if try_dest > 1:
      try_dest -= 1
    else:
      try_dest = max_cup
  dest = cups.index(try_dest)
  print "destination: " + str(try_dest)



  # Insert picked up cups at new destination
  dest = dest+1
  if dest > len(cups):
    dest = 0

  if dest < len(cups):
    cups[dest:dest] = pop_cups
  else:
    cups.extend(pop_cups)
  current_cup = cups.index(current_cup_val)

  print '' 

  # New current cup
  current_cup += 1
  if current_cup >= len(cups):
    current_cup = 0

  
print ""
print "-- final --"
  
printf('cups: ')
for i in range(0, len(cups)):
  if i == current_cup:
    printf('('+str(cups[i])+') ')
  else:
    printf(str(cups[i])+' ')
print ''

  
i = cups.index(1)
string = ''
for x in range(0, len(cups)-1):
  i+=1
  if i >= len(cups):
    i = 0
  string += str(cups[i]) 

print string
