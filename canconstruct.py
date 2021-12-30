def canconstruct (target, wordbank):
    if target == '' :
        return True
    a = -1
    for word in wordbank:
        try:
            a = target.index(word)
        except:
            a = -1
        if a == 0:
            var = target [len(word):] 
            print(var)
            if canconstruct (var, wordbank) == True:
                return True
    return False
#print(canconstruct('hellodear',['this', 'hello', 'kkh',  'ear' ,'d']))
print(canconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeff',
    ['e', 'eee', 'eeeee' ,'eeeeeee','eeeeeeeeee','eeeeeeeeeeeee']))