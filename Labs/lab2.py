'''Robert Brandl'''
'''I pledge my honor that I have abided by the Stevens Honor System.'''

def dot(L,K):
        '''assuming L,K are lists, return the dot product of L and K'''
        if L==[] or K ==[]:
            return 0.0
        else:
            return (L[0]*(K[0])) + dot(L[1:],K[1:])

def explode(S):
        '''assuming S is a string, return a list of characters in string S'''
        if S == '':
            return []
        else:
            return [S[0]] + explode(S[1:])
        
def ind(e,L):
        ''' assuming L is a list or string (the same with element e), return the index where e first appears in L, or the length if e is not present'''
        if L == [] or L == '':
            return 0
        
        elif L[0] == e:
            return 0
        else:
            return 1 + ind(e, L[1:])

def removeAll(e,L):
        '''assuming L is a list, returns a list identical to L, not containing elements identical to e'''
        if L == []:
            return []
        else:
            x = [L[0]]
            if L[0] == e:
                x = []
            return x + removeAll(e,L[1:])

def myFilter(func,L):
    '''assuming L is a list, return a list containing all elements of L which respond True when inputted into func'''
    if L == []:
        return []
    else:
        if (func(L[0])) == False:
            return myFilter(func,L[1:])
        else:
            return [L[0]] + myFilter(func,L[1:])

def deepReverse(L):
    '''assuming L is a list, return the reversal of the list where any list elements are also reversed within themselves'''
    if L == []:
        return []
    else:
        if isinstance(L[0], list):
            return deepReverse(L[1:]) + [deepReverse(L[0])]
        else:
            return deepReverse(L[1:]) + [L[0]]
        
