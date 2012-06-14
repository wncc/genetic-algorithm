import math


def fitnessFunction(citySequence,cities):

    sum = 0.0
    index = 0
    length = len(citySequence)
    while (index < length - 1):
        xcord = cities[(citySequence[index] - 1)][0] - cities[(citySequence[index + 1] - 1)][0]
        ycord = cities[(citySequence[index] - 1)][1] - cities[(citySequence[index + 1] - 1)][1]
        sum += math.sqrt((xcord * xcord) + (ycord * ycord))
        index += 1
    return sum

#print fitnessFunction([2,3,1],[[1,2],[2,3],[3,4]])
        
