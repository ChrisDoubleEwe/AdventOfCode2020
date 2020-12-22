import re 
import copy

dirs = ['N', 'E', 'S', 'W']
dir = 2
x = 0
y = 0

steps = []
with open("12_input.txt") as f:
  for line in f:
    match = re.search('([A-Z]{1})([0-9]*)', line)
    pair = []
    pair.append(match.group(1))
    pair.append(int(match.group(2)))
    steps.append(pair)


def change_direction(s):
  global dir
  turn = s[0]
  deg = s[1]
  amt = deg / 90
  for i in range(0, amt):
    if turn == 'R':
      dir += 1
      if dir > 4:
        dir = 1
    if turn == 'L':
      dir -= 1
      if dir < 1:
        dir = 4

for s in steps:
  this_dir = s[0]
  if s[0]=='R' or s[0]=='L':
    change_direction(s)
    continue

  if s[0]=='F':
    if dir == 1:
      this_dir = 'N'
    if dir == 2:
      this_dir = 'E'
    if dir == 3:
      this_dir = 'S'
    if dir == 4:
      this_dir = 'W'

  if this_dir == 'N':
    y += -1 *s[1]
  if this_dir == 'S':
    y += 1 *s[1]
  if this_dir == 'W':
    x += -1 *s[1]
  if this_dir == 'E':
    x += 1 *s[1]

  #print "x: " + str(x) + " ; y: " + str(y)

man = abs(x) + abs(y)
print man
    

