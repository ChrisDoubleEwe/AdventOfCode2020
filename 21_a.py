from printf import printf
import copy
import re 
import math

all_allergens = {}
all_ingrediants = []
food = []

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

with open("21_input.txt") as f:
  for line in f:
    l = line.strip()
    match = re.search('([a-z ]*) \(contains ([a-z, ]*)\)', l)
    ingredients = match.group(1).split(' ')
    food.append(ingredients)
    allergens = match.group(2).split(', ')

    for a in allergens:
      if a not in all_allergens.keys():
        all_allergens[a] = ingredients
      else:
        all_allergens[a] = intersection(all_allergens[a], ingredients)

    print ingredients
    all_ingrediants.extend(ingredients)
    all_ingrediants = sorted(set(all_ingrediants))
    print allergens


def all_unique():
  for a in all_allergens:
    if len(all_allergens[a]) > 1:
      return 0
  return 1

iter = 0
while all_unique() != 1:
  iter += 1
  if iter > 5:
    exit()
  print "Iteration : " + str(iter)
  print "-------------------------"
  print all_allergens
  for a in all_allergens:
    print "Checking : " + a
    if len(all_allergens[a]) == 1:
      print "   single entry"
      remove_allergen = all_allergens[a][0]
      print "Removing " + remove_allergen
      for z in all_allergens.keys():
        if (len(all_allergens[z]) > 1) and (remove_allergen in all_allergens[z]):
          all_allergens[z].remove(remove_allergen)
 
print all_allergens

print "CHECKING LIST"
allergen_list = []
for x in all_allergens.keys():
  allergen_list.append(all_allergens[x][0])

print "ALLERGEN LIST:"
print allergen_list
print "INGREDIANT LIST:"
print all_ingrediants
non_allergen_list = []
for x in all_ingrediants:
  if x in allergen_list:
    continue
  else:
    non_allergen_list.append(x)

print "\n\nNON ALLERGENS"
print non_allergen_list 

instances = 0
for f in food:
  for i in f:
    if i in non_allergen_list:
      instances+=1

print instances 
