'''Robert Brandl'''
'''I pledge my honor that I have abided by the Stevens Honor System.'''

from cs115 import *

def multiply (x,y):
    '''multiplies two numbers, x and y, together'''
    return x*y

def divides(n):
    ''' returns a function that checks whether a number divides n'''
    def div(k):
        return n % k == 0
    return div



def factorial(n):
    ''' assuming n>=0, return the product 1*2*...*n (n!)'''
    return reduce(multiply, range(1,n+1))
    
def mean(L):
    '''returns the average value in a list, assuming the list contains numbers'''
    def add(x,y):
        return x+y
    return (reduce(add,L))/len(L)

def prime(n):
    '''returns a boolean value, true if n is prime and false if n is composite'''
    return sum(map(divides(n), range(1,n+1))) == 2

    
