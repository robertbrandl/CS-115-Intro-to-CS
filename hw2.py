'''
Created on Sept 16, 2020
@author:   Robert Brandl
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
#from bigdict import *

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter, scorelist):
    '''assuming letter is a single character string and scorelist has the score associated with each letter, return the appropriate score/number for the given letter'''
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''assuming S is a string, return the score of the word according to the letter and scores in scorelist'''
    if S == "":
        return 0
    else:
        return letterScore(S[0],scorelist) + wordScore(S[1:], scorelist)
    
def letInWord(letters, wordLet):
    '''determines if the letter of a word matches a letter in Rack'''
    if letters == []:
        return ''
    elif wordLet in letters:
        return wordLet
    else:
        return ''

def removeLetter(e, L, repeat):
    '''removes specified letter from the list of letters, repeat acts a boolean to prevent multiple letters form being deleted'''
    if L == []:
        return []
    else:
        x = [L[0]]
        if L[0] == e and repeat == False:
            repeat = True
            x = []
        return x + removeLetter(e,L[1:], repeat)
        
def stringFromLetters(string, letters):
    '''determines what from the string can be made from the letters'''
    if string == '' or letters == '':
        return ''
    elif letInWord(letters,string[0]) == string[0]:
        letters = removeLetter(string[0],letters, False)
        return string[0] + stringFromLetters(string[1:],letters)
    else:
        return ''

def canStringBeMade(string, letters):
    '''determines if the string can be made from the list of letters'''
    if stringFromLetters(string,letters) == string:
        return True;
    else:
        return False;
    
def allWordsFromLetters(letters, Dict):
    '''returns a list of all possible words in Dict that can be made from the list of letters, letters'''
    return filter(lambda seq: canStringBeMade(seq,letters), Dict)

def scoreAndWord (word):
    '''returns a list consisting of the given word and its scrabble score'''
    return [word, wordScore(word, scrabbleScores)]
 
def scoreList(Rack):
    '''assuming Rack is a list of lowercase letters, return a list of lists consisting of each possible word - point combination using the letters in Rack'''
    return map(scoreAndWord, allWordsFromLetters(Rack,Dictionary))

def greaterThan(L1,L2):
    '''returns the list with the greater score'''
    if L1[1] >= L2[1]:
        return L1
    else:
        return L2
    
def bestWord(Rack):
    ''' assuming Rack is a list of lowercase letters, return a single list with two elements, the word with the highest score, and that score'''
    if Rack == []:
        return []
    elif scoreList(Rack) == []:
        return ['',0]
    return reduce(greaterThan, scoreList(Rack))
