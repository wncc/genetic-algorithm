import math

L=[ [1,1], [2,2], [1,3] ,[2,5] ]
print L
def fitness(source,destination):
    i=source-1
    j=destination-1
    int(i)
    int(j)
    x=L[i][0]-L[j][0]
    y=L[i][1]-L[j][1]
    distance=math.sqrt(x*x + y*y)
    return distance

trial=fitness(4,3)
print trial 
