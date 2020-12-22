import re 
import copy

map = []
c_len = 0
with open("11_input.txt") as f:
  for line in f:
    l = line.strip()
    row = []
    r_len = 0
    for c in l:
      row.append(c)
      r_len+=1
    map.append(row)
    c_len+=1

print "r_len: " + str(r_len)
print "c_len: " + str(c_len)


new_map = copy.deepcopy(map)
old_map = copy.deepcopy(map)


def print_map():
  global map
  print "-----------------------"
  for line in map:
    row = ''
    for c in line:
      row += c
    print row


def print_maps():
  global old_map
  global new_map
  print " *** OLD MAP ***"
  for line in old_map:
    row = ''
    for c in line:
      row += c
    print row

  print " *** NEW MAP ***"
  for line in new_map:
    row = ''
    for c in line:
      row += c
    print row



def flip():
  global map
  global new_map
  global old_map

  for r in range(0, len(map[0])):
    for c in range(0, len(map)):
      count = 0
      if (r > 0) and map[c][r-1]=='#':
        count+=1
      if (r < len(map[0])-1) and map[c][r+1]=='#':
        count+=1
      if (c > 0) and map[c-1][r]=='#':
        count+=1
      if (c < len(map)-1) and map[c+1][r]=='#':
        count+=1
      if (r > 0) and (c > 0) and map[c-1][r-1]=='#':
        count+=1
      if (r < len(map[0])-1) and (c > 0) and map[c-1][r+1]=='#':
        count+=1
      if (r > 0) and (c < len(map)-1) and map[c+1][r-1]=='#':
        count+=1
      if (r < len(map[0])-1) and (c < len(map)-1) and map[c+1][r+1]=='#':
        count+=1
      if (count==0) and (map[c][r]=='L'):
        new_map[c][r]='#'
      elif (count>=4) and (map[c][r]=='#'):
        new_map[c][r]='L'
      else:
        new_map[c][r]=map[c][r]
  old_map = copy.deepcopy(map)
  map = copy.deepcopy(new_map)

def diff_maps():
  global old_map
  global new_map

  #print "===DIFFING==========="
  #print_maps()

  diffs = 0
  for r in range(0, len(map[0])):
    for c in range(0, len(map)):
      if old_map[c][r] != new_map[c][r]:
        diffs+=1
  print diffs
  return diffs



print_map()
flip()
print_map()


while diff_maps() != 0:
  flip()
  print_map()

count = 0
for r in range(0, r_len):
  for c in range(0, c_len):
    if map[c][r] == '#':
      count+=1
print "======"
print count

