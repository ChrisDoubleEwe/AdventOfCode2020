import re 

class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

bags = {}
rules = []
all_bags = []
child_bags = []
root_bags = []

with open("07_input.txt") as f:
  for line in f:
    m = re.search('(.*) bags contain (.*)', line)
    if m:
      node_desc = m.group(1)
      if node_desc not in all_bags:
        all_bags.append(node_desc)
      children = m.group(2)

      child_nodes = []
      if children != "no other bags.":
        while children != '':
          m = re.search('([0-9]*) ([a-z]*) ([a-z]*) bag[s, \.]*(.*)', children)
          child_node_number = m.group(1)
          child_node_adj = m.group(2)
          child_node_col = m.group(3)
          child_node_desc = child_node_adj + " " + child_node_col
          if child_node_desc not in all_bags:
            all_bags.append(child_node_desc)
          if child_node_desc not in child_bags:
            child_bags.append(child_node_desc)


          remainder = m.group(4)
          child_pair = []
          child_pair.append(child_node_number)
          child_pair.append(child_node_desc)
          child_nodes.append(child_pair)

          children = remainder
      bags[node_desc]=child_nodes

 
for bag in all_bags:
  if bag not in child_bags:
    root_bags.append(bag)


paths = []

def process_path(paths, p, b):
  p.append(b)
  if bags[b] == []:
    paths.append(p)
    return p
  else:
    for child in bags[b]:
      process_path(paths, list(p), child[1])

  
all_paths = []
for bag in root_bags:
  paths = []
  path = []
  path = process_path(paths, path, bag)
  for x in paths:
    all_paths.append(x)


for x in all_paths:
  print x

all_containing_bags = []
for x in all_paths:
  if 'shiny gold' in x:
    sg_index = x.index('shiny gold')
    sg_index = sg_index - 1
    while sg_index >=0:
      all_containing_bags.append(x[sg_index])
      sg_index = sg_index - 1

print all_containing_bags
    
containers = sorted(set(all_containing_bags))
print containers
print len(containers)

total_bag_count = 0

def count_bags(b):
  global total_bag_count
  if bags[b] == []:
    return
  else:
    for child in bags[b]:
      print " - adding " + child[0] + " " + child[1]
      total_bag_count = total_bag_count + int(child[0])
      for i in range(0, int(child[0])):
        count_bags(child[1])
    return

count_bags('shiny gold')
print total_bag_count
