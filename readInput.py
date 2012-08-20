def readFile(city):

    f = open('./dj38.tsp.txt')
    line = f.readline()
    while ((not(line is '')) and  (line.find('NODE_COORD_SECTION'))<0):
        line=f.readline()
        
    line=f.readline()
    r=0
    
    while((line.find("EOF"))<0):
        L=list()
        L=line.split()
        city.append([float(L[1]),float(L[2])])
        r = r+1
        line=f.readline()



    
        

    
    


