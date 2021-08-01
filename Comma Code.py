
spam=['apples','bananas','tofu','cats']
def comma_code(a_list):
	for items in a_list:	
		list_minus_last = a_list[0:-1]
		if items in list_minus_last:
			print(items, end = ', ')
		else:
			print('and ' + str(items))
comma_code(spam)

