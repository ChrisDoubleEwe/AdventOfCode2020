content = []
with open("01_input.txt") as f:
  for line in f:
    content.append(int(line.strip('\n')))

for x in content:
  y = 2020 - x
  if y in content:
    print str(x) + " + " + str(y) + " = 2020";
    z = x * y
    print str(z)
    exit()

