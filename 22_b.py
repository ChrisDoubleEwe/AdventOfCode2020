from printf import printf
import copy
import re 
import math

p1_deck = []
p2_deck = []
game = 0

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
      p1_deck.append(int(l))
    else:
      p2_deck.append(int(l))

def make_key(a, b):
  k = 'aaa'
  for x in a:
    k+=str(x)
    k+='-'
  k+='xxx'
  for x in b:
    k+=str(x)
    k+='+'
  k+='zzz'
  return k

def play_game(g, p1_handx, p2_handx):
  p1_hand = []
  for i in p1_handx:
    p1_hand.append(i)
  p2_hand = []
  for i in p2_handx:
    p2_hand.append(i)


  game = g
  seen_hands = []
  break_infinite = 0
  round = 0

  if game > 1:
    all_nums = []
    all_nums.extend(p1_hand)
    all_nums.extend(p2_hand)
    m = max(all_nums)
    if m in p1_hand:
      dummy = 1
      #print "instant win for 1 because they have biggest card"
      #return 1


  while (len(p1_hand) > 0 ) and (len(p2_hand) > 0):
    round += 1
    print "Player 1's deck: " + str(p1_hand)
    print "Player 2's deck: " + str(p2_hand)

    hands = []
    hands.append(copy.deepcopy(p1_hand))
    hands.append(copy.deepcopy(p2_hand))
    if hands in seen_hands:
      # Player 1 instant win
      print "Instant win for player 1, based on infinite recursion"
      return 1
    else:
      seen_hands.append(hands)

    p1_card = p1_hand.pop(0)
    print "Player 1 plays: " + str(p1_card)
    p2_card = p2_hand.pop(0)
    print "Player 2 plays: " + str(p2_card)

    round_winner = -1
    if (len(p1_hand) >= p1_card) and (len(p2_hand) >= p2_card):
      print "Playing a sub-game to determine the winner..."
      p1_copy_hand = []
      p2_copy_hand = []
      for i in range(0, p1_card):
        p1_copy_hand.append(p1_hand[i])
      for i in range(0, p2_card):
        p2_copy_hand.append(p2_hand[i])

      round_winner = play_game(game+1, p1_copy_hand, p2_copy_hand)
    else:
      if p1_card > p2_card:
        round_winner = 1
      else:
        round_winner = 2

    if round_winner == 1:
      #print "Player 1 wins round " + str(round) + " of game " + str(game) + "!"
      p1_hand.append(p1_card)
      p1_hand.append(p2_card)
    else:
      #print "Player 2 wins round " + str(round) + " of game " + str(game) + "!"
      p2_hand.append(p2_card)
      p2_hand.append(p1_card)
    #print ''

    if game > 1:
      if ((len(p1_hand) == 0 ) or (len(p2_hand) == 0)):
        if len(p1_hand) > 0:
          return 1
        else:
          return 2
    if game == 1:
      if ((len(p1_hand) == 0 ) or (len(p2_hand) == 0)):
        print "== Post-game results =="
        print "Player 1's deck: " + str(p1_hand)
        print "Player 2's deck: " + str(p2_hand)

        w = []
        if len(p1_hand) > 0:
          w = copy.deepcopy(p1_hand)
        else:
          w = copy.deepcopy(p2_hand)
        w.reverse()
        multiplier = 1
        sum = 0
        for i in w:
          sum += (i * multiplier)
          multiplier += 1

        print sum



winner = play_game(1, p1_deck, p2_deck)

