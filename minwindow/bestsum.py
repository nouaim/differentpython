def howSum (targetsum, Array):
	#print(targetsum)

	if targetsum == 0 :
		return [] 
	if targetsum < 0 :
		return None

	shortestsum = None
	
	for n in Array :
		remainder = targetsum - n

		result = howSum (remainder, Array ) 

		if result != None:
			combination= [*result, n]

			if shortestsum == None or len(combination)< len(shortestsum):
				shortestsum = combination

	return shortestsum	

print (howSum (3 , [1,2]))
#print (howSum (8 , [2,3,5]))
#print (howSum (300 , [7,14]))