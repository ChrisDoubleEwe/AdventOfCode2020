content = []
with open("01_input.txt") as f:
  for line in f:
    content.append(int(line.strip('\n')))

for x in content:
  y = 2020 - x
  print "Got " + str(x)+ "  Looking for 2 numbers that make " + str(y)
  for a in content:
    b = y - a
    print "  Got " + str(a) + ", looking for " + str(b)
    if b in content:
      print "    Found it!"
      print str(x) + " + " + str(a) + " + " + str(b) + "= 2020";
      z = x * a * b
      print str(z)
      exit()

