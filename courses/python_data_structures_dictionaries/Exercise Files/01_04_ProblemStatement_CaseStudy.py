#getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv
with open('treeorderssubsetnodupes.csv', mode='r') as infile:
    reader = csv.reader(infile)
   #creating a dictionary - walk through code.
   # And introduce the idea of a Case Study
    mydict ={}
    

    for row in reader:
        key = row[0]
        mydict[key]=row[1]
        
   
    
    infile.close()
    	

    	
