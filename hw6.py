'''
Created on 10/14/2020
@author:   Robert Brandl
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
from cs115 import *
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def numToBinary(n):
    '''Returns the string with the binary representation of non-negative integer n. If n is 0, the empty string is returned.'''
    if n==0: return ''
    elif n % 2 == 1: return numToBinary(n//2) + '1'
    else: return numToBinary(n//2) + '0'
    
def binaryToNum(s):
    '''Returns the integer corresponding to the binary representation in s. Note: the empty string represents 0.'''
    num = 1
    def binToNum(s,num):
        if s == '': return 0
        else: return int(s[-1])* num + binToNum(s[:-1],num*2)
    return binToNum(s,num)

def addZero(S):
    '''adds the needed zeros to make S a five digit binary number'''
    return (COMPRESSED_BLOCK_SIZE-len(S))*'0' + S

def countBinDigits(S,n):
    '''counts how many binary digits occur consecutively'''
    if S == '' or S[0] != n: return 0
    else: return 1 + countBinDigits(S[1:],n)

def compress(S):
    '''returns the run length encoding form binary string of S as output'''
    def comp(S,binDigit):
        if S == '': return '' 
        totalDig = countBinDigits(S,binDigit)
        if totalDig > MAX_RUN_LENGTH: totalDig = MAX_RUN_LENGTH
        return addZero(numToBinary(totalDig)) + comp(S[totalDig:], str(1-(int(binDigit))))
    return comp(S,'0')
    
def uncompress(C):
    '''returns the binary string representing the run length encoding binary string C'''
    def uncomp(C,binDigit):
        if C =='': return ''
        return binaryToNum(C[:COMPRESSED_BLOCK_SIZE]) * binDigit + uncomp(C[COMPRESSED_BLOCK_SIZE:], str(1-int(binDigit)))
    return uncomp(C,'0')

def compression(S):
    '''ratio of compressed to uncompressed'''
    return len(compress(S))/len(S)
