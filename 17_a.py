from printf import printf
import copy
import re 

width = 50
offset = int(width/2)

cube = []
new_cube = []
for z in range(0, width):
  square = []
  for y in range(0, width):
    row = []
    for x in range(0, width):
      row.append('.')
    square.append(row)
  cube.append(square)

def count_neighbors(z, y, x):
  count = 0
  for z_off in range (-1, 2):
    for y_off in range (-1, 2):
      for x_off in range (-1, 2):
        if z_off == y_off == x_off == 0:
          continue
        if cube[z+z_off][y+y_off][x+x_off] == '#':
          count += 1
  return count
 
def advance():
  global cube
  new_cube = copy.deepcopy(cube)
  for z in range(1, width-1):
    for y in range(1, width-1):
      for x in range(1, width-1):
        n = count_neighbors(z, y, x)
        if cube[z][y][x] == '#':
          if n<2 or n>3:
            new_cube[z][y][x] = '.'
        elif cube[z][y][x] == '.':
          if n == 3:
            new_cube[z][y][x] = '#'
  cube = copy.deepcopy(new_cube)




def count_active():
  count = 0
  for z in range(0, width):
    for y in range(0, width):
      for x in range(0, width):
        if cube[z][y][x] == '#':
          count+=1
  return count


def print_cube():
  for z in range(0, width):
    empty = 1
    for y in range(0, width):
      for x in range(0, width):
        if cube[z][y][x] == '#':
          empty = 0
    if empty == 1:
      continue
    print z - offset
    for y in range(0, width):
      for x in range(0, width):
        printf(str(cube[z][y][x]))
      print ''
    print '\n\n'


print_cube()
      

with open("17_input.txt") as f:
  y = -1
  for l in f:
    y+=1
    in_width = len(l.strip())
    start_x = (width - in_width ) / 2 
    x = start_x -1
    for c in l.strip():
      x += 1
      cube[offset][start_x+y][x]=c

print_cube()

for i in range(1, 7):
  print "=== Iteration " + str(i) + " ========="
  advance()
  print_cube() 

print count_active()
