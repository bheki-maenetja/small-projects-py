
sal_data_keys = ["Austin", "Portland", "Dallas","Atlanta"] 
sal_data_values = [91185,110123, 89123, 112000] 

sal_info = {}
print("#### Creating a dictionary without using comprehension")
for key, value in zip(sal_data_keys,sal_data_values):
	sal_info[key] = value
print (sal_info)
#sal_info.clear()

#Using Dictionary Comprehension to popultate the dictionary








#filtering through the dictionary using comprehension
