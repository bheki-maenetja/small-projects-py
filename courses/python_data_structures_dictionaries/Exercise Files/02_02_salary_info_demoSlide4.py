sal_info= dict ()
sal_info={'Los Angeles':110459,'Austin':911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 89286}
'''
print (sal_info.get ('Dallas',"not found"))
print (sal_info.get('Portland',"not found"))


print (sal_info.keys())

print (sal_info.values())


print ("Key-Value pair")
for k,v in sal_info.items():
	print ("the Key is ", k, "the Value is ", v)



print ("City with highest Salary " + max(sal_info, key=sal_info.get))


print ("City with lowest Salary " + min(sal_info, key=sal_info.get))

# alternates to the del operator follow:
print (sal_info)
print ("Value of key " + str(sal_info.pop('Dallas', "not found")))
print (sal_info)

print (sal_info.popitem())
print (sal_info)

'''
#prints dictionary with keys sorted
print (sal_info)
print ( sorted(sal_info.keys()))
print (sorted(sal_info.values()))




