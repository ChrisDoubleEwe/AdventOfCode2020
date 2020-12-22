import re 
import copy

dirs = ['N', 'E', 'S', 'W']
dir = 1
x = 0
y = 0

way_x = 10
way_y = -1

steps = []
with open("12_input.txt") as f:
  for line in f:
    match = re.search('([A-Z]{1})([0-9]*)', line)
    pair = []
    pair.append(match.group(1))
    pair.append(int(match.group(2)))
    steps.append(pair)

def change_direction(s):
  global way_x
  global way_y
  turn = s[0]
  deg = s[1]
  amt = deg / 90
  for i in range(0, amt):
    tmp_x = way_x
    tmp_y = way_y
    if turn == 'R':
      way_x = -1 * tmp_y
      way_y = tmp_x 
    if turn == 'L':
      way_x = tmp_y
      way_y = -1 * tmp_x

for s in steps:
  this_dir = s[0]
  mod_x = 0
  mod_y = 0
  if s[0]=='R' or s[0]=='L':
    change_direction(s)
    continue

  if s[0]=='F':
    for i in range(0, s[1]):
      x += way_x
      y += way_y
      continue

  if this_dir == 'N':
    mod_y = -1 *s[1]
    mod_x = 0
  if this_dir == 'S':
    mod_y = 1 *s[1]
    mod_x = 0
  if this_dir == 'W':
    mod_x = -1 *s[1]
    mod_y = 0
  if this_dir == 'E':
    mod_x = 1 *s[1]
    mod_y = 0
  way_x += mod_x
  way_y += mod_y

print "x: " + str(x) + " ; y: " + str(y)

man = abs(x) + abs(y)
print man
    

