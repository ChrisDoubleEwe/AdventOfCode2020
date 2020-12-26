from printf import printf
import copy
import re 
import math

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
 
print tiles

# Normalize directions
opposites = [['e', 'w'], ['se', 'nw'], ['sw',  'ne']]

result_tiles = []
tile_num = 0
for tile in tiles:
  tile_num +=1
  print "TILE: " + str(tile_num)
  print "========================"
  print "Doing: " + str(tile)
  for x in range(0, 100):
    for pair in opposites:
      while pair[0] in tile and pair[1] in tile:
        print "Removing pair: " + str(pair)
        tile.pop(tile.index(pair[0]))
        tile.pop(tile.index(pair[1]))
        print tile
    while 'se' in tile and 'ne' in tile:
        print "Replacing se-ne with e triple "
        tile.pop(tile.index('se'))
        tile.pop(tile.index('ne'))
        tile.append('e')
        print tile
    while 'sw' in tile and 'nw' in tile:
        print "Replacing sw-nw with w " 
        tile.pop(tile.index('sw'))
        tile.pop(tile.index('nw'))
        tile.append('w')
        print tile
    while 'sw' in tile and 'e' in tile:
        print "Replace sw-e with se "
        tile.pop(tile.index('sw'))
        tile.pop(tile.index('e'))
        tile.append('se')
        print tile
    while 'nw' in tile and 'e' in tile:
        print "Replace nw-e with ne "
        tile.pop(tile.index('nw'))
        tile.pop(tile.index('e'))
        tile.append('ne')
        print tile
    while 'se' in tile and 'w' in tile:
        print "Replace se-w with sw "
        tile.pop(tile.index('se'))
        tile.pop(tile.index('w'))
        tile.append('sw')
        print tile
    while 'ne' in tile and 'w' in tile:
        print "Replace ne-w with nw "
        tile.pop(tile.index('ne'))
        tile.pop(tile.index('w'))
        tile.append('nw')
        print tile




  print "Sorting:"
  tile_sorted=sorted(tile)
  tile = tile_sorted
  print tile
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



print result_tiles
count = 0
for i in result_tiles:
  count += 1
  print str(count) + " " + i
print len(result_tiles)

unique_tiles = []
for i in result_tiles:
  count = 0
  for j in result_tiles:
    if i == j:
      count += 1
  if count%2 == 1:
    unique_tiles.append(i)

print i
print "NUMBER OF BLACK TILES"
print len(unique_tiles)

  
