def howSum (targetsum, Array, memo={}):
	#print(targetsum)
	if targetsum in memo:
		return memo[targetsum]

	if targetsum == 0 :
		return [] 
	if targetsum < 0 :
		return None

	shortestsum = None

	for n in Array :
		remainder = targetsum - n

		memo[targetsum] = howSum (remainder, Array , memo) 



		if memo[targetsum] != None:
			combination = [*memo[targetsum], n]

			if shortestsum == None or len(combination)< len(shortestsum):
				shortestsum = combination
	return shortestsum	

#print (howSum (3 , [1,2]))
#print (howSum (8 , [2,3,5]))
print (howSum (300 , [7,14]))