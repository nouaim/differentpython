def Binary_search(mat, item):
    found = False
    last = len(mat)-1
    first = 0
    a= input()
    while (first<= last) and not found:
    	mid = (last + first) // 2
    	if (mat[mid] == item):
    		found = True
    	else:
    		if(item  < mat[mid]):
    			first = first - 1
    		else: 
    			first= mid + 1 
    return found
print(Binary_search([9,10,11,12,13,14,15], 9))