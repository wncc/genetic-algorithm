import random

def randomSwap(seq):
    l = len(seq)
    ind1 = random.randint(1,l) - 1
    ind2 = random.randint(1,l) - 1
    temp = seq[ind1]
    seq[ind1] = seq[ind2]
    seq[ind2] = temp
    return seq
    
def eq(l1,l2):
    i=0
    a=True
    for i in range(len (l1)-1):
        if(l1[i]!=l2[i]):
            a= False
            break
    return a

def mutate(seq):
    if(random.randint(1,100) == random.randint(1,100)):
        seq = randomSwap(seq)
    return seq
i=0        


