import re 
x_incr = 3
y_incr = 1
row = []
map = []
rows = 0
cols = 0
content = []
with open("03_input.txt") as f:
  for line in f:
    cols = 0
    for c in line.strip('\n'):
      row.append(c)
      cols = cols + 1
    map.append(row)
    row = []
    rows = rows + 1

#test_x = 1
#test_y = 10
#print map[test_y][test_x]

pos_x = 0
pos_y = 0

tree_count = 0

while pos_y < rows:
  print "Pos: x= " + str(pos_x) + " ; y= " + str(pos_y)
  if map[pos_y][pos_x] == '#':
    print "  TREE HIT!"
    tree_count = tree_count + 1
  else:
    print "  No tree hit"
  pos_x = pos_x + x_incr
  if pos_x >= cols:
    pos_x = pos_x - cols
  pos_y = pos_y + y_incr

print "Trees hit: " + str(tree_count)
    
