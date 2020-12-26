from printf import printf
import copy
import re 
import math

input = '389125467'
input = '219347865'
 
limit = 1000000

current_cup = -1
max_cup = 0
cups = {}
first = -1
last = -1
for i in input:
  if int(i) > max_cup:
    max_cup = int(i)
  if first < 0:
    first = int(i)
    current_cup = first
  if last > 0:
    cups[int(last)] = int(i)
  last = int(i)

for j in range(max_cup+1, limit+1):
  cups[last] = j
  last = j

max_cup = limit
cups[max_cup] = first
  

print "max_cup: " + str(max_cup)

#cups[last] = first

moves = 10000000

this_move = 0
while this_move < moves:
  this_move += 1
  if this_move % 100000 == 0:
    print "-- move " + str(this_move) + "  (" + str((this_move * 100) / 10000000) +  "%) "
  #print cups
  # Get current cup
  #print "current cup : " + str(current_cup)
  next_1 = cups[current_cup]
  next_2 = cups[next_1]
  next_3 = cups[next_2]
  next_4 = cups[next_3]
  
  #print "pick up: " + str(next_1) + ", " + str(next_2) + ", " + str(next_3) 


  # Work out destination cup 
  try_dest = current_cup
  if try_dest > 1:
    try_dest -= 1
  else:
    try_dest = max_cup
  #print "initial try dest : " + str(try_dest)


  #print next_1
  #print next_2
  #print next_3
  while try_dest == next_1 or try_dest == next_2 or try_dest == next_3:
    #print "loop try dest : " + str(try_dest)

    if try_dest > 1:
      try_dest -= 1
      #print "sub 1"
    else:
      try_dest = max_cup
      #print "set max"

  # Insert picked up cups at new destination
  #print "DESTINATION : " + str(try_dest)
  dest = try_dest
  remember_link = cups[dest]
  cups[dest] = next_1
  cups[next_3] = remember_link
  cups[current_cup] = next_4


  #print '' 

  # New current cup
  new_current_cup = cups[current_cup]
  current_cup = new_current_cup

  
#print ""
print "-- final --"
 
#print cups 
next_1 = cups[1]
next_2 = cups[next_1]
print "RESULT"
print next_1 * next_2

