import re 
import copy

data1 = [0,3,6]
data2 = [1,3,2]
data3 = [2,1,3]
data4 = [1,2,3]
data5 = [2,3,1]
data6 = [3,2,1]
data7 = [3,1,2]
data = [0,12,6,13,20,1,17]
data = list(data)

seen = {}
before = {}
numbers = []
turn = 0
this_num = 0
while len(data) > 0 :
  turn += 1
  this_num = data.pop(0)
  seen[this_num] = turn
  before[this_num]=0
  numbers.append(this_num)



while True:
  if turn%100000 == 0:
    print turn
  if turn == 2020:
    print "SPOKEN NUMBER 2020: " + str(numbers[len(numbers)-1])
    exit()

  turn += 1
  this_num = numbers[len(numbers)-1]

  if this_num not in before:
    before[this_num] = 0
    seen[this_num]=turn-1
    numbers.append(0)
    continue



  if before[this_num]==0:
    if seen[this_num] == turn-1:
      # Never seen before
      before[this_num]=seen[this_num]
      seen[this_num]=turn-1
      numbers.append(0)
    else:
      # Seen before
      diff = turn - 1 - seen[this_num]
      before[this_num]=seen[this_num]
      seen[this_num]=turn-1
      numbers.append(diff)
  else:
    # Seen before
    diff = turn - 1 - seen[this_num]
    before[this_num]=seen[this_num]
    seen[this_num]=turn-1
    numbers.append(diff)

  
