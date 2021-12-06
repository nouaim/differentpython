from collections import Counter
def MinWindowSubstring(N):

	a=N[0]
	b=N[0]
	c=[]
	for i in range (0, len(N[0])):
		for j in range (0 , len(N[1])):

			if (N[0][i] == N[1][j]):
				c = N[0][i] + c


print(MinWindowSubstring(["aaabaaddae", "aed"]))
