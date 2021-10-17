#Robert Brandl
#I pledge my honor that I have abided by the Stevens Honor System.

def mult(c, n):
    """ mult uses only a loop and addition to multiply c by the integer n """
    result = 0
    for x in range(n):
        result = result + c
    return result

def update(c, n):
    """ update starts with z=0 and runs z = z**2 + c for a total of n times. It returns the final z."""
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    '''takes a complex number c and integer n, return True if c is in Mandelbrot set'''
    z = 0 + 0j
    for x in range(n):
        if abs(z) > 2: return False
        z = z**2 + c
    return True
