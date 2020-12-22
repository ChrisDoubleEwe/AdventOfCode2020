x=-1

data=[23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,647,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,x,x,x,x,x,x,29,x,557,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17]

ta=939

t=1006726



dataa=[7,13,x,x,59,x,31,19]



y=[]

for x in data:

  if x !=-1:

      y.append(x)

      


min =10000000

id=0

for i in y:

    z=t%i

    if z > 0:

        f=i-z

        z=f

    if z<min:

        min=z

        id=i


        

print id*min


