from printf import printf
import copy
import re 
import math

floor_size = 125
floor = []

for i in range(0, floor_size):
  row = []
  for j in range(0, floor_size):
    row.append('.')
  floor.append(row)

def print_floor():
  print '\n------------------------------------\n'
  global floor
  for i in floor:
    for j in i:
      printf(str(j))
    print ''


tiles = []
two_fac = ''
with open("24_input.txt") as f:
  for line in f:
    l = line.strip()
    this = []
    for c in l:
      if c == 'n' or c == 's':
        two_fac = c
      else:
        if two_fac != '':
          two_fac += c
          this.append(two_fac)
          two_fac = ''
        else:
          this.append(c)
    tiles.append(this)
 

# Normalize directions
opposites = [['e', 'w'], ['se', 'nw'], ['sw',  'ne']]

result_tiles = []
tile_num = 0
for tile in tiles:
  tile_num +=1
  for x in range(0, 100):
    for pair in opposites:
      while pair[0] in tile and pair[1] in tile:
        tile.pop(tile.index(pair[0]))
        tile.pop(tile.index(pair[1]))
    while 'se' in tile and 'ne' in tile:
        tile.pop(tile.index('se'))
        tile.pop(tile.index('ne'))
        tile.append('e')
    while 'sw' in tile and 'nw' in tile:
        tile.pop(tile.index('sw'))
        tile.pop(tile.index('nw'))
        tile.append('w')
    while 'sw' in tile and 'e' in tile:
        tile.pop(tile.index('sw'))
        tile.pop(tile.index('e'))
        tile.append('se')
    while 'nw' in tile and 'e' in tile:
        tile.pop(tile.index('nw'))
        tile.pop(tile.index('e'))
        tile.append('ne')
    while 'se' in tile and 'w' in tile:
        tile.pop(tile.index('se'))
        tile.pop(tile.index('w'))
        tile.append('sw')
    while 'ne' in tile and 'w' in tile:
        tile.pop(tile.index('ne'))
        tile.pop(tile.index('w'))
        tile.append('nw')




  tile_sorted=sorted(tile)
  tile = tile_sorted
  result_string = ''
  for i in tile:
    if i == 'e' or i == 'w':
      result_string+=str(i)
    if i == 'se':
      result_string+='S'
    if i == 'sw':
      result_string+='s'
    if i == 'ne':
      result_string+='N'
    if i == 'nw':
      result_string+='n'
  result_tiles.append(result_string)



count = 0
for i in result_tiles:
  count += 1

unique_tiles = []
for i in result_tiles:
  count = 0
  for j in result_tiles:
    if i == j:
      count += 1
  if count%2 == 1:
    unique_tiles.append(i)

print "NUMBER OF BLACK TILES"
print len(unique_tiles)

current_x=floor_size / 2
current_y=floor_size / 2

#     e f 
#    d 1 a
#     c b    
# 
#     ef
#     d1a
#      cb


def move(x, y, dir):
  new_x = x
  new_y = y
  if dir == 'ne':
    new_x = x
    new_y = y-1
  if dir == 'nw':
    new_x = x-1
    new_y = y-1
  if dir == 'se':
    new_x = x+1
    new_y = y+1
  if dir == 'sw':
    new_x = x
    new_y = y+1
  if dir == 'e':
    new_x = x+1
    new_y = y
  if dir == 'w':
    new_x = x-1
    new_y = y
  pair = []
  pair.append(new_x)
  pair.append(new_y)
  return pair
  
floor[current_y][current_x] = '0'

for path in unique_tiles:
  current_x=floor_size / 2
  current_y=floor_size / 2

  for d in path:
    if d == 'n':
      current_x = move(current_x, current_y, 'nw')[0]
      current_y = move(current_x, current_y, 'nw')[1]
    if d == 'N':
      current_x = move(current_x, current_y, 'ne')[0]
      current_y = move(current_x, current_y, 'ne')[1]
    if d == 's':
      current_x = move(current_x, current_y, 'sw')[0]
      current_y = move(current_x, current_y, 'sw')[1]
    if d == 'S':
      current_x = move(current_x, current_y, 'se')[0]
      current_y = move(current_x, current_y, 'se')[1]
    if d == 'e':
      current_x = move(current_x, current_y, 'e')[0]
      current_y = move(current_x, current_y, 'e')[1]
    if d == 'w':
      current_x = move(current_x, current_y, 'w')[0]
      current_y = move(current_x, current_y, 'w')[1]
  floor[current_y][current_x] = '#'

def count_neighbours(x, y):
  count_black = 0
  count_white = 0

  for d in ['nw', 'ne', 'se', 'sw', 'e', 'w']:
    tmp=move(x, y, d)
    if tmp[0] < 0 or tmp[1] < 0 or tmp[0] >= floor_size or tmp[1] >= floor_size:
      continue
    if floor[tmp[1]][tmp[0]] == '.':
      count_white += 1
    if floor[tmp[1]][tmp[0]] == '#':
      count_black += 1
  return count_black


def count_black():
  global floor
  min_x = floor_size
  min_y = floor_size
  max_x = 0
  max_y = 0

  count = 0
  for x in range(0, floor_size):
    for y in range(0, floor_size):
      if floor[y][x] == '#':
        count += 1
        if y < min_y:
          min_y = y
        if y > max_y:
          max_y = y
        if x < min_x:
          min_x = x
        if x > max_x:
          max_x = x


  #print "min x = " + str(min_x)
  #print "max x = " + str(max_x)
  #print "min y = " + str(min_y)
  #print "max y = " + str(max_y)

  return count

def evolve():
  global floor
  new_floor = copy.deepcopy(floor)
  for x in range(0, floor_size):
    for y in range(0, floor_size):
      count = count_neighbours(x, y)
      if floor[y][x] == '.' and count == 2:
        new_floor[y][x] = '#'
      elif floor[y][x] == '#' and (count == 0 or count > 2):
        new_floor[y][x] = '.'
      else:
        new_floor[y][x] = floor[y][x]
  floor = copy.deepcopy(new_floor)

for x in range(1, 101):
  evolve()
  #print_floor()
  print "Day " + str(x) + ": " + str(count_black())
