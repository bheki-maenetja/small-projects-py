
sal_data_keys = ["Austin", "Portland", "Dallas","Atlanta"] 
sal_data_values = [91185,110123, 89123, 112000] 

sal_info = {}
print("#### Creating a dictionary without using comprehension")
for key, value in zip(sal_data_keys,sal_data_values):
	sal_info[key] = value
print (sal_info)
#sal_info.clear()


#alternate to filtering the dictionary using a for loop

sal_100k ={}
for k in sal_info:
 if sal_info[k] > 100000:
  sal_100k[k] = sal_info[k]

print (sal_100k)
#sal_100k.clear()



#filtering through the dictionary using comprehension
