from printf import printf
import copy
import re 
import math

p1_hand = []
p2_hand = []

with open("22_input.txt") as f:
  player = 0
  for line in f:
    l = line.strip()
    match = re.search('Player ([1-2]):', l)
    if match:
      player = int(match.group(1))
      continue
    if l == '':
      continue
    if player == 1:
      p1_hand.append(int(l))
    else:
      p2_hand.append(int(l))

round = 0
while (len(p1_hand) > 0 ) and (len(p2_hand) > 0):
  round += 1
  print "-- Round " + str(round) + " --"
  print "Player 1's deck: " + str(p1_hand)
  print "Player 2's deck: " + str(p2_hand)

  p1_card = p1_hand.pop(0)
  print "Player 1 plays: " + str(p1_card)
  p2_card = p2_hand.pop(0)
  print "Player 2 plays: " + str(p2_card)

  if p1_card > p2_card:
    print "Player 1 wins the round!"
    p1_hand.append(p1_card)
    p1_hand.append(p2_card)
  else:
    print "Player 2 wins the round!"
    p2_hand.append(p2_card)
    p2_hand.append(p1_card)
  print ''

print ''
print "== Post-game results =="
print "Player 1's deck: " + str(p1_hand)
print "Player 2's deck: " + str(p2_hand)

winning_hand = []

if len(p1_hand) > 0:
  winning_hand = copy.deepcopy(p1_hand)
if len(p2_hand) > 0:
  winning_hand = copy.deepcopy(p2_hand)


winning_hand.reverse()
multiplier = 1
sum = 0
for i in winning_hand:
  sum += (i * multiplier) 
  multiplier += 1

print sum


