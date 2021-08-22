 #getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv


with open('TreeOrdersSubset.csv', mode='r') as infile:
    reader = csv.reader(infile)
    treeOrders = {}      # dict has key as subdivison id, and value as the count of trees 
    for row in reader:
        key = row[0]    #Sudvidision id
        
        if (key not in treeOrders):
            treeNum = row[1]
            treeOrders[key] = int(treeNum)

        else:
            treeNum= row[1]
            prev_count = treeOrders[key]
            treeOrders[key]= int (prev_count) + int (treeNum)

infile.close()
print ("length of dictionary ",len(treeOrders))
#Create a new dict treeOrders10 with subdivisions that have more than 10 tree orders
#use dict comprehension

