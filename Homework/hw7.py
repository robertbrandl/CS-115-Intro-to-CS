#Robert Brandl
#I pledge my honor that I have abided by the Stevens Honor System.

def numToBaseB(N,B):
    '''returns the decimal value N into a value of base B'''
    def helper(N,B):
        '''helper performs numToBaseB without added zeros'''
        if N==0: return ''
        elif N % B == 0: return helper(N//B,B) + '0'
        else: return helper((N-N%B)//B,B) + str(N%B)
    if N==0: return '0'
    else: return helper(N,B)

def baseBToNum(S, B):
    '''returns the decimal version of S (of base B)'''
    if S == '': return 0
    return int(S[0])*(B**(len(S)-1)) + baseBToNum(S[1:],B)

def baseToBase(B1,B2,SinB1):
    '''returns sinB1 in B1 to the value in B2'''
    if SinB1 == '': return 0
    return numToBaseB(baseBToNum(SinB1,B1),B2)

def add(S,T): 
    '''returns S + T in binary form'''
    if S == '' or T == '': return 0
    return numToBaseB(baseBToNum(S,2)+baseBToNum(T,2),2)

def addB(S,T):
    '''takes two binary strings and returns the strings added together'''
    def addhelper(S,T,carry):
        '''assists addB by using a carrybit'''
        if S=='' or T == '': return carry if carry == '1' else ''
        elif S[-1] == T[-1]:
            if S[-1] == '1' and carry == '0': return addhelper(S[:-1],T[:-1],'1') + '0'
            elif S[-1] == '1' and carry == '1': return addhelper(S[:-1],T[:-1],'1') + '1'
            elif S[-1] == '0' and carry == '1': return addhelper(S[:-1],T[:-1],'0') + '0'
            return addhelper(S[:-1],T[:-1],'0') + '1'
        return addhelper(S[:-1],T[:-1],'0') + '1' if carry == '0' else addhelper(S[:-1],T[:-1],'1') + '0'
    if T == '': return S
    elif S == '': return T
    elif len(S) == len(T): return addhelper(S,T,'0')
    elif len(S) > len(T):
        T = '0'*(len(S)-len(T)) + T
        return addhelper(S,T,'0')
    else:
        S = '0'*(len(T)-len(S)) + S
        return addhelper(S,T,'0')
