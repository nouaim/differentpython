def howSum (targetsum, Array, memo ={}):

	if targetsum == 0 :
		return [] 
	if targetsum < 0 :
		return None

	if targetsum in memo:
		return memo[targetsum]

	for n in Array :
		remainder = targetsum - n

		result = howSum (remainder, Array ) 
		if result != None:
			memo [targetsum] = [*result, n]
			return memo [targetsum]
	memo[targetsum] = None
	return None

#print (howSum (3 , [1,2]))
#print (howSum (8 , [2,3,5]))
print (howSum (300 , [7,14]))