from printf import printf
import copy
import re 
import math

#card_public_key = 5764801
#door_public_key = 17807724

card_public_key = 14222596
door_public_key = 4057428

card_loop_size = -1
door_loop_size = -1

def transform(x, loop):
  result = 1
  for i in range(0, loop):
    result = result * x 
    result = result % 20201227
  return result

def transform2(x, target):
  print "Starting..."
  result = 1
  for i in range(0, 10000000):
    print "LOOP " + str(i)
    result = result * x
    result = result % 20201227
    if result == target:
      print "LOOP SIZE: " + str(i+1)
      break
  if result == target:
    return i+1
  else:
    print "RANGE EXCEEDED"
  return -1

card_loop_size = transform2(7, card_public_key)
door_loop_size = transform2(7, door_public_key)

if (card_loop_size == -1) or (door_loop_size == -1):
  exit()


print "ENCRYPTION KEY: "
print "door public key: " + str(door_public_key)
print "door loop size: " + str(door_loop_size)
print "card public key: " + str(card_public_key)
print "card loop size: " + str(card_loop_size)

encrypt_key = transform(card_public_key, door_loop_size)
encrypt_check = transform(door_public_key, card_loop_size)

print encrypt_key
print encrypt_check

