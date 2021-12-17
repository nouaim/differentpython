def MinWindowSubstring(N):
	dictionary = {}
	dictionary2= {}
	lista = ['','','','']
	strings= ''
	for a in N[1]:
		if a in dictionary2:
			dictionary2[a] += 1
		else:
		    dictionary2[a] = 1
	print(dictionary2)	
	print("length of the 2nd dict: ",len(dictionary2))
	c= 0




## Taget abc     
## Input: alkcbjabc  First case
## Input: aaaxdbbckglo  Second case
    
## We need a list to save "words where letters ppear in N[1]"

	for a in N[0]:
		strings += a
		print("string is : ",strings)
		
		if a in dictionary:
			dictionary[a] += 1
		else:
		    dictionary[a] = 1
		print("dictionary is : ",dictionary)
		sss= {x:dictionary2[x] for x in dictionary2 if x in dictionary}

		if sss
		print("sss is : ",sss)
		# if strings.intersection(strings):
		# 	break

		
		# if strings.count(a) <= N[1].count(a) : ## il faut utiliser le premier dictionaire
		# 	c+=1


		# if c == len(dictionary2):
		# 	break

		# if a not in N[1] and len(strings) == 1:
		# 	strings = ''
	print(dictionary)

	print("minimum string is : ", strings)

	print('c = ',c)
MinWindowSubstring(['aaabacdkdaekac', 'kac'])

# N=["aaabacdkdae", "aedk"]


# lista = [kcfa, cka ,lcghka]
# if len(lista[a]) == len (N[1]):
# 	break
# 	return lista[a]

##Try starting from the big and minice - instead

'''strings  = N[0][0]  ## Here we add strings by using + 
strings2 = N[0][1]
cout = 0
a=1

while 
	strings = strings + N[0][a]
	strings2+= N[0][a+1]
	print(strings)
	a+=1
	'''
	# # strings += N[0][a]
	# # if strings.count(N[a]) == N[1].count(N[a]): 
	# # 	strings = min(strings, strings2)
	# # return strings
	# # 	if N[0][a] in N[1]:
	# # 		strings += N[0][a]
	# # 		print(strings)
	# 	else:
	# 		strings += strings2 + N[0][a] 
	# 	#strings = min(strings, strings2)
	# 	if strings 

# for a in range (0, len(N[0])):
# 	if N[0][a] in N[1] :
# 		strings += N[0][a]
# 	elif N[0][a] not in N[1] and strings == N[1]:
# 		strings+= N[0][a]
# 	strings2 += N[0][a]

# print(strings)
# print(strings2)