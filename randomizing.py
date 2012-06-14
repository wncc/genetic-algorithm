import random


def randomize(n):
    l = range(n + 1)
    m=[1]
    del l[0:2]
    k=n-1
    for i in range(0,k):
        j=random.randint(0,k-1)
        m.append(l[j])
        del l[j]
        i+=1
        k-=1

    return m




