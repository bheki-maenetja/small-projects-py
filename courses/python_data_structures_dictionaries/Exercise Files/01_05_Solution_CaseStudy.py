#getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv
with open('treeorderssubsetnodupes.csv', mode='r') as infile:
    reader = csv.reader(infile)
   #1st Video - creating a dictionary - walk them through this. And introduce the idea of a Case Study
    mydict ={}
    

    for row in reader:
        key = row[0]
        mydict[key]=row[1]
        
    #print (mydict)
    
    sizeOfDi = len(mydict)
    print (sizeOfDi)
    #print ("The dictionary is of size: " + str(sizeOfDi))

    #code for modifying a key - we will take the example of 281
    
    mydict['205']=10
    print(mydict)
    
    #code for adding a key-value pair
    mydict['999']=12
    print (mydict)

    for i in mydict:
        print (i, mydict[i])

    
    
    infile.close()
    	

    	
