import re 
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

def count_trees(x, y):
  pos_x = 0
  pos_y = 0
  tree_count = 0

  while pos_y < rows:
    #print "Pos: x= " + str(pos_x) + " ; y= " + str(pos_y)
    if map[pos_y][pos_x] == '#':
      tree_count = tree_count + 1
    pos_x = pos_x + x
    if pos_x >= cols:
      pos_x = pos_x - cols
    pos_y = pos_y + y
  return tree_count

total = 0
a = count_trees(1, 1)
b = count_trees(3, 1)
c = count_trees(5, 1)
d = count_trees(7, 1)
e = count_trees(1, 2)

print "Trees hit: " + str(a)
print "Trees hit: " + str(b)
print "Trees hit: " + str(c)
print "Trees hit: " + str(d)
print "Trees hit: " + str(e)
    
total = a*b*c*d*e

print "TOTAL : " + str(total)
