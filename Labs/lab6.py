'''
Created on 10/14/2020
@author:   Robert Brandl
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 != 0

#42 in base 2: 101010
#Even in base 10: rightmost bit will be 0 in binary, 1 in odd
#Removing the rightmost bit will result in a binary number equivalent to integer division by 2 of the decimal answer


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'
    
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    num = 1
    def binToNum(s,num):
        if s == '':
            return 0
        else:
            return int(s[-1])* num + binToNum(s[:-1],num*2)
    return binToNum(s,num)

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    st = numToBinary(binaryToNum(s)+1)
    if len(s)-len(st) == -1: return st[1:]
    return (len(s)-len(st))*'0' + st

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print (s)
    if n == 0: return #
    else: return count(increment(s),n-1)
        

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif n % 3 == 2: return numToTernary(n//3) + '2'
    elif n % 3 == 1: return numToTernary(n//3) + '1'
    else: return numToTernary(n//3) + '0'

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    num = 1
    def terToNum(s,num):
        if s == '':
            return 0
        else:
            return int(s[-1])* num + terToNum(s[:-1],num*3)
    return terToNum(s,num)
