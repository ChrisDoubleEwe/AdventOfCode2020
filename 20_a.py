from printf import printf
import copy
import re 

tiles = {}

def convert_to_bin(s):
  s = s.replace('.', '0')
  s = s.replace('#', '1')
  return s

def reverse(s):
  r = s[::-1]
  return r

edges = []
tile_num = -1
num_tiles = 0
with open("20_input.txt") as f:
  for line in f:
    l = line.strip()
    if l == '':
      continue
    if ':' in l:
      match = re.search('Tile ([0-9]*):', l)
      tile_num = int(match.group(1))
      print tile_num
      row = 0
      continue
    if row == 0:
      top = l
      print "top: " + top
      left = l[0]
      right = l[9]
      row+=1
      continue
    if row == 9:
      bot = l
      left += l[0]
      right += l[9]
      print "bot: " + bot
      print "left: " + left
      print "right: " + right
      row+=1
      edges.append(top)
      edges.append(left)
      edges.append(right)
      edges.append(bot)
      edges.append(reverse(top))
      edges.append(reverse(left))
      edges.append(reverse(right))
      edges.append(reverse(bot))
      tiles[tile_num] = []
      tiles[tile_num].append(top)
      tiles[tile_num].append(bot)
      tiles[tile_num].append(left)
      tiles[tile_num].append(right)
      tiles[tile_num].append(reverse(top))
      tiles[tile_num].append(reverse(bot))
      tiles[tile_num].append(reverse(left))
      tiles[tile_num].append(reverse(right))
 
      num_tiles +=1
      continue
    left += l[0]
    right += l[9]
    row+=1
 

print "all edges: " + str(len(edges))
unique_edges = sorted(set(edges))
print "unique edges: " + str(len(unique_edges))

max_unique_edges = 0
for tile in tiles.keys():
  num_unique_edges = 0
  for edge in tiles[tile]:
    occ = edges.count(edge)
    if occ == 1:
      num_unique_edges +=1
  if num_unique_edges > max_unique_edges:
    max_unique_edges = num_unique_edges


result = 1
for tile in tiles.keys():
  num_unique_edges = 0
  for edge in tiles[tile]:
    occ = edges.count(edge)
    if occ == 1:
      num_unique_edges +=1
  if num_unique_edges == max_unique_edges:
    print tile
    result = result * tile

print "RESULT"
print "============"
print result

