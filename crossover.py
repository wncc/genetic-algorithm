import math

def isValid(elem,seq):
    return  not(elem in seq)

def distanceSqd(elem1,elem2, cityList):
    x=cityList[elem1 - 1][0] - cityList[elem2 - 1][0]
    y=cityList[elem1 - 1][1] - cityList[elem2 - 1][1]
    return (x*x + y*y)

def list2toN(n):
    ans1=[2]
    i=3
    while(i <= n):
        ans1.append(i)
        i+=1
    return ans1

def crossover(seq1,seq2,cityList):
    length = len(seq1)
    ans = [1]
    lengthAns = 1
    e1=0
    e2=0
    while(lengthAns<length):
        lastElem = ans[lengthAns - 1]
        ind1= seq1.index(lastElem)
        ind2= seq2.index(lastElem)
        for  e1 in seq1[ind1 + 1:]:
                if(isValid(e1,ans)):
                    break
        else:
            for e1 in list2toN(length):
                if(isValid(e1,ans)):
                    break
        for e2 in seq2[ind2 + 1:]:
            if(isValid(e2, ans)):
                break
        else:
            for e2 in list2toN(length):
                if(isValid(e2,ans)):
                    break
        d1=distanceSqd(e1,lastElem,cityList)
        d2=distanceSqd(e2,lastElem,cityList)
        if(d1<d2):
            ans.append(e1)
            lastElem=e1
            lengthAns+=1
        else:
            ans.append(e2)
            lastElem=e2
            lengthAns+=1

    return ans



citylist = [[1,2],[3,4],[5,6],[3,3]]
seq1=[1,4,3,2]
seq2=[1,3,4,2]
a= list2toN(5)

#print crossover(seq1,seq2,citylist)
