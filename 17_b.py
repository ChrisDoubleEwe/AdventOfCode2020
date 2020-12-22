from printf import printf
import copy
import re 

width = 50
offset = int(width/2)

hypercube = []
new_hypercube = []
for w in range(0, width):
  cube = []
  for z in range(0, width):
    square = []
    for y in range(0, width):
      row = []
      for x in range(0, width):
        row.append('.')
      square.append(row)
    cube.append(square)
  hypercube.append(cube)

def count_neighbors(w, z, y, x):
  count = 0
  for w_off in range (-1, 2):
    for z_off in range (-1, 2):
      for y_off in range (-1, 2):
        for x_off in range (-1, 2):
          if w_off == z_off == y_off == x_off == 0:
            continue
          if hypercube[w+w_off][z+z_off][y+y_off][x+x_off] == '#':
            count += 1
  return count
 
def advance():
  global hypercube
  new_hypercube = copy.deepcopy(hypercube)
  for w in range(1, width-1):
    for z in range(1, width-1):
      for y in range(1, width-1):
        for x in range(1, width-1):
          n = count_neighbors(w, z, y, x)
          if hypercube[w][z][y][x] == '#':
            if n<2 or n>3:
              new_hypercube[w][z][y][x] = '.'
          elif hypercube[w][z][y][x] == '.':
            if n == 3:
              new_hypercube[w][z][y][x] = '#'
  hypercube = copy.deepcopy(new_hypercube)




def count_active():
  count = 0
  for w in range(0, width):
    for z in range(0, width):
      for y in range(0, width):
        for x in range(0, width):
          if hypercube[w][z][y][x] == '#':
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



with open("17_input.txt") as f:
  y = -1
  for l in f:
    y+=1
    in_width = len(l.strip())
    start_x = (width - in_width ) / 2 
    x = start_x -1
    for c in l.strip():
      x += 1
      hypercube[offset][offset][start_x+y][x]=c

#print_cube()

for i in range(1, 7):
  print "=== Iteration " + str(i) + " ========="
  advance()
  #print_cube() 

print count_active()
