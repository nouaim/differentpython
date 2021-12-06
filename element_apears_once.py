# Given a non-empty list of integers, 
# every element appears twice except for one. Find that single one.
def function_w (list1):
	c= {}
	for a in list1:
		if a in c:
			c[a] += 1
		else:	
			c[a] = 1
	return print (min(c, key=c.get))	

function_w([1,2,1,4,2,3,3,4,5,6,6])


## OTher possible solution 

# numbers = [1, 1, 2, 2, 3, 3, 4, 5, 5]
# count = {}
# for i in numbers:
#     if i not in count:
#         count[i] = 1
#     else:
#         count[i] += 1

# for key, value in count.items():
#     if value == 1:
#         print(key)