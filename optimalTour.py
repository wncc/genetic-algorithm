import fitnessFunction
import readInput

def readFile(city):

    f = open('./ALL_tsp/a280.opt.tour')
    line = f.readline()
    while ((not(line is '')) and  (line.find('TOUR_SECTION'))<0):
        line=f.readline()
        
    line=f.readline()
    r=0
    L=list()
    L=line.split()
    print L
    val = int(L[0])

    while(val > 0):
        city.append(val)
        line=f.readline()
        L=line.split()
        r = r+1
        val = int(L[0])

coordinates = []
city = []
readFile(city)

print city

readInput.readFile(coordinates)

print coordinates

print "Optimum tour length is: ", fitnessFunction.fitnessFunction(city, coordinates)
