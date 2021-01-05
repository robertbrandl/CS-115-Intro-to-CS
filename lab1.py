#Robert Brandl CS115
#I pledge my honor that I have abided by the Stevens Honor System.

from cs115 import *
import math

def inverse(n):
    '''returns a floating point number for the reciprocal of n (1/n), n must be a floating point or integer value'''
    return 1.0/n

def e(n):
    '''returns a floating point value for the Taylor approximation of e^n, n must be a positive whole number'''
    return sum(map(inverse,(map(math.factorial,range(n+1)))))

def error(n):
    ''' returns the absolute value of the difference between the "actual" value of e and the approximation in the e(n) function assuming that n terms are used'''
    def subtract(x,y):
        return x - y
    return abs(reduce(subtract, [math.e, e(n)]))
