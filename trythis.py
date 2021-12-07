def single(aList):
    for item in aList:
        if aList.count(item) == 1:
            return print(item)
single([4,1,4,1,3])