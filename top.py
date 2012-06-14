import fitnessFunction

def quickSort(sortBy,sortAlong):
    pivot = sortBy[0]
    pivotAlong = sortAlong[0]
    length = len(sortBy)
    lhsBy = []
    rhsBy = []
    lhsAlong = []
    rhsAlong = []
    
    
    for i in range(1,length):
        if(sortBy[i] < pivot):
            lhsBy.append(sortBy[i])
            lhsAlong.append(sortAlong[i])
        else:
            rhsBy.append(sortBy[i])
            rhsAlong.append(sortAlong[i])
    
    if(len(lhsBy) > 0):
        (lhsBy, lhsAlong) = quickSort(lhsBy, lhsAlong)
    
    if(len(rhsBy) > 0):
        (rhsBy, rhsAlong) = quickSort(rhsBy, rhsAlong)

    sortBy = lhsBy + [pivot] + rhsBy
    sortAlong = lhsAlong + [pivotAlong] + rhsAlong

    return (sortBy, sortAlong)


def insertAtPosition(fitness, member, fitnessArr, memberArr):
    length = len(fitnessArr)
    for i in range(length):
        if fitness < fitnessArr[i]:
            j = length - 1
            while (j > i):
                fitnessArr[j] = fitnessArr[j - 1]
                memberArr[j] = memberArr[j - 1]
                j -= 1
    
            fitnessArr[i]= fitness
            memberArr[i]= member
            break


# this function gives you the n top most cities in the current new generation
# members is the new generation
# cities is the co ordinates
def top(n,members,cityList):
    
    fitnessList = []
    for member in members:
        fitnessList.append(fitnessFunction.fitnessFunction(member, cityList))
#        print fitnessFunction.fitnessFunction(member, cityList), " ", member    
#    print fitnessList
    ans = []
    ansFitness = []
    insertedMembers = 0
    memberCount = len(members)

    for i in range(n):
        ans.append(members[i])
        ansFitness.append(fitnessList[i])

    (ansFitness,ans) = quickSort(ansFitness, ans)
    

    threshold = ansFitness[n - 1]
    
    for j in range(n, memberCount):
        if fitnessList[j] < threshold:
            insertAtPosition(fitnessList[j], members[j], ansFitness, ans)
            threshold = ansFitness[n - 1]

    return ans

#print top(3,[[1,2,3,4],[1,3,2,4],[1,4,3,2],[1,2,4,3],[1,3,4,2],[1,4,2,3]],[[1,2],[3,4],[1,3],[3,5]])
    
l1= [1,2,4,2,1,0,-7]    
l2= [2,3,4,5,5,7,8]
(l1,l2) = quickSort(l1,l2)

#print "qs", l1, l2
