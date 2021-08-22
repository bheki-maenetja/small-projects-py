eng_di = {}
#Adding lists as value
eng_di['solitude']= ['lone', 'lonely', 'alone', 'unaccompanied', 'without society']
eng_di['hope']= ['aspiration', 'desire', 'wish', 'expectation', 'ambition']
print (eng_di)


#Creating a dictionary with an empty list
eng_di.clear()
eng_di = {'solitude':[]}
eng_words = ['lone', 'lonely', 'alone', 'unaccompanied', 'without society']
eng_di['solitude'].append(eng_words[0])
print (eng_di)

eng_di['solitude']= eng_words
print (eng_di)


if (eng_di.get('solitude')):
	for list_item in eng_di['solitude']:
		print (list_item)
else:
	print ("word not in dictionary")

