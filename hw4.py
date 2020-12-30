'''Robert Brandl'''
'''I pledge my honor that I have abided by the Stevens Honor System.'''
from cs115 import *
def pascal_row(num):
    '''returns a list of the numbers in the pascal row at row of integer num'''
    if num == 0:
        return [1]
    else:
        p = pascal_row(num-1)
        return [1] + map(lambda x: p[x] + p[x+1], range(len(p)-1)) + [1]

def pascal_triangle(num):
    ''' returns a list of lists containing the values of the all the rows up to and including row n'''
    if num == 0:
        return [[1]]
    else:
        return pascal_triangle(num-1) + [pascal_row(num)]

def test_pascal_row():
    ''' uses assert statements to check whether the function pascal_row works accurately'''
    assert(pascal_row(0) == [1])
    assert(pascal_row(1) == [1,1])
    assert(pascal_row(5) == [1,5,10,10,5,1])
    assert(pascal_row(2) == [1,2,1])

def test_pascal_triangle():
    ''' uses assert statements to check whether the function pascal_triangle works accurately'''
    assert(pascal_triangle(0) == [[1]])
    assert(pascal_triangle(1) == [[1],[1,1]])
    assert(pascal_triangle(2) == [[1],[1,1],[1,2,1]])
    assert(pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
