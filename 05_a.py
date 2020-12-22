content = []
ids = []
with open("05_input.txt") as f:
  for line in f:
    content.append(line.strip('\n'))

for x in content:
  col = x[7:]
  row = x[:-3]
  
  row = row.replace('F', '0')
  row = row.replace('B', '1')
  col = col.replace('L', '0')
  col = col.replace('R', '1')
  row_int = int(row, 2)
  col_int = int(col, 2)


  id = (row_int * 8) + col_int
  ids.append(id)

max = sorted(ids)[-1]
print max
