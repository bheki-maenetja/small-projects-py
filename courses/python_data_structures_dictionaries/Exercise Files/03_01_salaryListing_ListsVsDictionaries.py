sal_info_keys = ["Austin", "Portland", "Dallas"] 
sal_info_values = [91185,110123, 89123] 

# Printing original keys-value lists 
print ("Original key list is : " + str(sal_info_keys)) 
print ("Original value list is : " + str(sal_info_values)) 
# to convert lists to dictionary 

sal_info={}

print ("#### Method 1 using for in ")
indx = 0 
for key in sal_info_keys:
	value = sal_info_values[indx]
	sal_info[key] = value
	indx=indx+1

# Printing resultant dictionary 
print ("Resultant dictionary is : " + str(sal_info))





