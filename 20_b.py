from printf import printf
import copy
import re 
import math

tiles = {}
squares = {}
squares_edges = {}

def reverse(s):
  r = s[::-1]
  return r

edges = []
tile_num = -1
num_tiles = 0
this_square = []
this_square_edges = []

with open("20_input.txt") as f:
  for line in f:
    l = line.strip()
    if l == '':
      continue
    if ':' in l:
      match = re.search('Tile ([0-9]*):', l)
      tile_num = int(match.group(1))
      row = 0
      continue
    if row == 0:
      this_square = []
      this_square.append(l)
      top = l
      left = l[0]
      right = l[9]
      row+=1
      continue
    if row == 9:
      bot = reverse(l)
      left += l[0]
      right += l[9]
      row+=1
      left = reverse(left)
      this_square.append(l)
      edges.append(top)
      edges.append(left)
      edges.append(bot)
      edges.append(right)
      edges.append(reverse(top))
      edges.append(reverse(right))
      edges.append(reverse(bot))
      edges.append(reverse(left))
      tiles[tile_num] = []
      tiles[tile_num].append(top)
      tiles[tile_num].append(left)
      tiles[tile_num].append(bot)
      tiles[tile_num].append(right)
      tiles[tile_num].append(reverse(top))
      tiles[tile_num].append(reverse(right))
      tiles[tile_num].append(reverse(bot))
      tiles[tile_num].append(reverse(left))
      squares[tile_num] = this_square
      squares_edges[tile_num] = []
      squares_edges[tile_num].append(top)
      squares_edges[tile_num].append(left)
      squares_edges[tile_num].append(bot)
      squares_edges[tile_num].append(right)
      squares_edges[tile_num].append(reverse(top))
      squares_edges[tile_num].append(reverse(right))
      squares_edges[tile_num].append(reverse(bot))
      squares_edges[tile_num].append(reverse(left))

      num_tiles +=1
      continue
    left += l[0]
    right += l[9]
    this_square.append(l)
    row+=1
 

unique_edges = sorted(set(edges))

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
start_tile = -1
for tile in tiles.keys():
  num_unique_edges = 0
  for edge in tiles[tile]:
    occ = edges.count(edge)
    if occ == 1:
      num_unique_edges +=1
  if num_unique_edges == max_unique_edges:
    print "FOUND CORNER: " + str(tile)
    result = result * tile
    start_tile = tile


available_tiles = []
for s in squares.keys():
  available_tiles.append(s)

result_tiles = []
result_flip = []
result_rot = []
result_tiles.append(tile)
result_flip.append(0)
result_rot.append(0)
#available_tiles.remove(start_tile)

this_tile_num = 1
match_dir = 1
this_tile_id = start_tile

result_grid = []
result_squares = []
for x in range(0, int(math.sqrt(num_tiles))):
  square_row = []
  row0 = []
  row1 = []
  row2 = []
  row3 = []
  row4 = []
  row5 = []
  row6 = []
  row7 = []
  row8 = []
  row9 = []
  for y in range(0, int(math.sqrt(num_tiles))):
    square_row.append('')
    row0.extend(['+', '-', '-', '-', '-', '-', '-', '-', '-', '+'])
    row1.extend(['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'])
    row2.extend(['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'])
    row3.extend(['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'])
    row4.extend(['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'])
    row5.extend(['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'])
    row6.extend(['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'])
    row7.extend(['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'])
    row8.extend(['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'])
    row9.extend(['+', '-', '-', '-', '-', '-', '-', '-', '-', '+'])
  result_grid.append(row0)
  result_grid.append(row1)
  result_grid.append(row2)
  result_grid.append(row3)
  result_grid.append(row4)
  result_grid.append(row5)
  result_grid.append(row6)
  result_grid.append(row7)
  result_grid.append(row8)
  result_grid.append(row9)
  result_squares.append(square_row)


def print_grid():
  print "----------------------------------------------------------------------------------"
  x_count = 0
  y_count = 0
  for i in result_grid:
    if y_count%10==0:
      print ''
    y_count+=1
    for j in i:
      if x_count%10==0:
        printf(' ')
      printf(j)
      x_count+=1
    print ''

def print_new_grid():
  print "----------------------------------------------------------------------------------"
  x_count = 0
  y_count = 0
  for i in new_result_grid:
    y_count+=1
    for j in i:
      printf(j)
      x_count+=1
    print ''


print_grid()

def insert_result_square(x_box, y_box, current_result):
  for x in range(0, 10):
    for y in range(0, 10):
      result_grid[(y_box*10)+y][(x_box*10)+x] = current_result[y][x]
 
def insert_result(x_box, y_box, this_tile_id, rot, flip):
  str_grid = squares[this_tile_id]
  current_result = []
  for x in str_grid:
    this_row = []
    for c in x:
      this_row.append(c)
    current_result.append(this_row)

  final_result = copy.deepcopy(current_result)

  flip_copy = copy.deepcopy(squares[this_tile_id])

  if flip == 1:
    for x in range(0, 10):
      current_result[x] = copy.deepcopy(final_result[9-x])
 
  rot_copy = copy.deepcopy(current_result)
  while rot > 0:
    rot_copy = copy.deepcopy(current_result)
    rot=rot-1
    for x in range(0, 10):
      for y in range(0, 10):
        rot_copy[y][9-x]=current_result[x][y]
    current_result=copy.deepcopy(rot_copy) 

  final_result = copy.deepcopy(current_result)

  for x in range(0, 10):
    for y in range(0, 10):
      result_grid[(y_box*10)+y][(x_box*10)+x] = final_result[y][x]

  print_grid()
  
 
# FIND TOP LEFT SQUARE, WITH CORRECT ROTATION AND ORIENTATION AGAINST ITS 2 MATCHES
print "This tile: " + str(this_tile_id)
available_tiles.remove(this_tile_id)
print available_tiles
found = 0


orig_square = copy.deepcopy(squares[this_tile_id])
flip_square = copy.deepcopy(squares[this_tile_id])
flip_square.reverse()


found = 0
this_square = copy.deepcopy(orig_square)
current_result = []
for x in this_square:
  this_row = []
  for c in x:
    this_row.append(c)
  current_result.append(this_row)

for rot in range(0, 4):
  right_edge = ''
  for x in current_result:
    right_edge+=str(x[9])
    bot_edge = ''.join(current_result[9]) 
  print "  Looking for right_edge: " + right_edge
  for x in available_tiles:
    for y in available_tiles:
      if x == y :
        continue
      if right_edge in squares_edges[x] and bot_edge in squares_edges[y]:
        if found == 0:
          insert_result_square(0, 0, current_result)
          result_squares[0][0] = this_tile_id
        found = 1
  rot_copy = copy.deepcopy(current_result)
  for x in range(0, 10):
    for y in range(0, 10):
      rot_copy[y][9-x]=current_result[x][y]
  current_result=copy.deepcopy(rot_copy)

this_square = copy.deepcopy(flip_square)
current_result = []
for x in this_square:
  this_row = []
  for c in x:
    this_row.append(c)
  current_result.append(this_row)

for rot in range(0, 4):
  right_edge = ''
  for x in current_result:
    right_edge+=str(x[9])
    bot_edge = ''.join(current_result[9])
  for x in available_tiles:
    for y in available_tiles:
      if x == y :
        continue
      if right_edge in squares_edges[x] and bot_edge in squares_edges[y]:
        if found == 0:
          insert_result_square(0, 0, current_result)
          result_squares[0][0] = this_tile_id
        found = 1
  rot_copy = copy.deepcopy(current_result)
  for x in range(0, 10):
    for y in range(0, 10):
      rot_copy[y][9-x]=current_result[x][y]
  current_result=copy.deepcopy(rot_copy)

print_grid()

for x in result_squares:
  print x

def convert_to_array(l):
  current_result = []
  for d in l:
    this_row = []
    for c in d:
      this_row.append(c)
    current_result.append(this_row)
  return(current_result)

def get_left_edge(l):
  left_edge = ''
  for z in l:
    left_edge+=str(z[0])
  return(left_edge)

def get_top_edge(l):
  return(''.join(l[0]))


def rotate_tile(t):
  rot_copy = copy.deepcopy(t)
  for x in range(0, 10):
    for y in range(0, 10):
      rot_copy[y][9-x]=t[x][y]
  return(rot_copy)

for y in range(0, len(result_squares)):
  for x in range(0, len(result_squares)):
    if result_squares[y][x] != '':
      print "Skipping"
      print result_squares[y][x]
      continue
    print "Doing x=" + str(x) + " y=" + str(y)
    if x > 0:
      # MATCH LEFT
      existing_tile_id=result_squares[y][x-1]
      existing_right_edge = ''
      for z in range(0, 10):
        existing_right_edge+= result_grid[(y*10)+z][((x-1)*10)+9]

      for tile in available_tiles:
        if existing_right_edge in squares_edges[tile]:
          result_squares[y][x] = tile
          available_tiles.remove(tile)
          break;

      matching_tile = convert_to_array(squares[tile])
      flip_square = copy.deepcopy(squares[tile])
      flip_square.reverse()
      matching_flip_tile = convert_to_array(flip_square)

      found = 0
      for rot in range(0, 4):
        if (get_left_edge(matching_tile)) == existing_right_edge:
          if found == 0:
            insert_result_square(x, y, matching_tile)
            found = 1
        matching_tile = rotate_tile(matching_tile)
      for rot in range(0, 4):
        if (get_left_edge(matching_flip_tile)) == existing_right_edge:
          if found == 0:
            insert_result_square(x, y, matching_flip_tile)
            found = 1
        matching_flip_tile = rotate_tile(matching_flip_tile)

    else:
      # MATCH DOWN
      existing_tile_id=result_squares[y-1][x]
      existing_bot_edge = ''
      for z in range(0, 10):
        existing_bot_edge+= result_grid[((y-1)*10)+9][(x*10)+z]

      for tile in available_tiles:
        if existing_bot_edge in squares_edges[tile]:
          result_squares[y][x] = tile
          available_tiles.remove(tile)
          break;

      matching_tile = convert_to_array(squares[tile])
      flip_square = copy.deepcopy(squares[tile])
      flip_square.reverse()
      matching_flip_tile = convert_to_array(flip_square)

      found = 0
      for rot in range(0, 4):
        if (get_top_edge(matching_tile)) == existing_bot_edge:
          if found == 0:
            insert_result_square(x, y, matching_tile)
            found = 1
        matching_tile = rotate_tile(matching_tile)
      for rot in range(0, 4):
        if (get_top_edge(matching_flip_tile)) == existing_bot_edge:
          if found == 0:
            insert_result_square(x, y, matching_flip_tile)
            found = 1
        matching_flip_tile = rotate_tile(matching_flip_tile)

      


print_grid()
for x in result_squares:
  print x 


dim = len(result_grid)

new_result_grid = []
for y in range(0, dim):
  new_line = []
  for x in range(0, dim):
    if (x%10 != 0) and (x%10 != 9):
     new_line.append(result_grid[y][x])
  if (y%10 != 0) and (y%10 != 9):
    new_result_grid.append(new_line)

print_new_grid()
   
dim = len(new_result_grid)
 

seamonster=[[0,18], [1,0], [1,5], [1,6], [1,11], [1,12], [1,17], [1,18], [1,19], [2,1], [2,4], [2,7], [2,10], [2,13], [2,16]]

def check_grid():
  total = 0
  for y in range(0, dim-2):
    for x in range(0, dim-19):
      found = 1
      for pair in seamonster:
        if new_result_grid[y+pair[0]][x+pair[1]]!='#':
          found = 0
      if found == 1:
        print "FOUND"
        total += 1
  return total

def rotate_new_grid():
  global new_result_grid
  rot_copy = copy.deepcopy(new_result_grid)
  d = len(new_result_grid)
  z = d -1
  for x in range(0, d):
    for y in range(0, d):
      rot_copy[y][z-x]=new_result_grid[x][y]
  new_result_grid = copy.deepcopy(rot_copy)



current_total = 0
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
if check_grid() > current_total:
  final_grid = copy.deepcopy(new_result_grid)
rotate_new_grid()

if check_grid() > current_total:
  final_grid = copy.deepcopy(new_result_grid)
rotate_new_grid()

if check_grid() > current_total:
  final_grid = copy.deepcopy(new_result_grid)
rotate_new_grid()

if check_grid() > current_total:
  final_grid = copy.deepcopy(new_result_grid)
rotate_new_grid()
flip_new_grid = copy.deepcopy(new_result_grid)
flip_new_grid.reverse()
new_result_grid = copy.deepcopy(flip_new_grid)

if check_grid() > current_total:
  final_grid = copy.deepcopy(new_result_grid)
rotate_new_grid()

if check_grid() > current_total:
  final_grid = copy.deepcopy(new_result_grid)
rotate_new_grid()

if check_grid() > current_total:
  final_grid = copy.deepcopy(new_result_grid)
rotate_new_grid()

if check_grid() > current_total:
  final_grid = copy.deepcopy(new_result_grid)


new_result_grid = copy.deepcopy(final_grid)


def replace_seamonster():
  for y in range(0, dim-2):
    for x in range(0, dim-19):
      found = 1
      for pair in seamonster:
        if new_result_grid[y+pair[0]][x+pair[1]]!='#':
          found = 0
      if found == 1:
        for pair in seamonster:
          new_result_grid[y+pair[0]][x+pair[1]]='O'

replace_seamonster()
print_new_grid()



rough = 0
for x in new_result_grid:
  for c in x:
    if c == '#':
      rough +=1
print rough
