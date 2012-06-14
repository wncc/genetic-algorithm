import randomizing

def randomLists(n,cityCount):
    ans=[]
    for i in range(n):
        ans.append(randomizing.randomize(cityCount))
    return ans
