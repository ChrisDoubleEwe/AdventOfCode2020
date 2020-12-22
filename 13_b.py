
x=-1
data1=[23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,647,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,x,x,x,x,x,x,29,x,557,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17]
target1=1006726

data2=[7,13,x,x,59,x,31,19]
target2=939

data3=[17,x,13,19]
target3=3417

data4=[67,7,59,61]
target4=754018

data5=[67,x,7,59,61]
target5=779210

data6=[67,7,x,59,61]
target6=1261476

data7=[1789,37,47,1889]
target7=1202161486

data=[]
for b in data1:
   data.append(b)


t = 0
m = data[0]
max_period = data[0]
sync_index = 0
sync_first = -1
syncing_index = -1

iter = 0
while True:
  iter +=1
  found = 1
  t+=m
  for i in range(0, len(data)):
    if data[i] < 0:
      continue
    if ((t+i)%data[i])!=0:
      found = 0
      break
    else:
      if i > sync_index:
        if sync_first < 0:
          sync_first = t
          syncing_index = i
        else:
          if i == syncing_index:
            m = t - sync_first


            sync_index = i
            syncing_index = -1
          sync_first = -1

                
  if found == 1:
    print "RESULT======"
    print t
    exit()

