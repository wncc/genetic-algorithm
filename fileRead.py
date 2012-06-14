
f = open('./dj38.tsp.txt')
line = f.readline()
firstword=""



while ((not(line is '')) and  (line.find('NODE_COORD_SECTION'))<0):
    
    line=f.readline()

line=f.readline()

while((line.find("EOF"))<0):
    line=f.readline()

print "Last line is : " , line
print "finished reading."


    
        

    
    


