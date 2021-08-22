sal_info= dict ()
sal_info={'Austin':911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 89286,'Portland':101367}

#reassigns the salary for Atlanta
sal_info['Atlanta']= 92340
print (sal_info)

#del sal_info['Atlanta']
#print (sal_info)

#print (sal_info['Atlanta'])
#del sal_info

#sal_info.clear()
#print (sal_info)


if ('Seattle' not in sal_info):
	sal_info['Seattle']= 110340
else:
	print ("key exists")

print (sal_info)
























#if ("Austin" in sal_db):
#	print (sal_db['Austin'])

#if ("Seattle" not in sal_db):
#	sal_db['Seattle']= 100010




#print (sal_db)


#del sal_db['Dallas']
#print (sal_db['Dallas'])
#del sal_db
#print (sal_db)
