from collections import Counter
def MinWindowSubstring(N):
    a=N[0]
    b=N[0]
    c=N[0][0]
    print(Counter(N[1]))
    print(Counter(N[0]))
    
    for i in range (1,len(N[0])):
        c = c+ N[0][i] 

        ## if counter (a[1] et a[2]) = 0 de counter(k) ---> start from a [2]
        print(c)
        if ( Counter(c) == Counter(N[1])):
            print("We are all good")
        else:
            print("we are not well") 
            print(Counter(c))  
    # for i in range (1,len(N[0])):
    # 	a[0][i] = N[0][i]
    # 	a.count(N[i])
    # 	x = N[i].count(9)
    # 	print(x)
    # return x
MinWindowSubstring(["aaabaaddae", "aad"])
