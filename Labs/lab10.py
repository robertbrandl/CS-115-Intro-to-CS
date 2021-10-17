#Robert Brandl
#I pledge my honor that I have abided by the Stevens Honor System.
import sys
import random
from cs115 import *
def createOneRow(width):
    """ returns one row of zeros of width "width"...
    You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    '''except first and last line and border make inner cells 1'''
    A=createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row==0 or col==0 or row==h-1 or col==w-1: A[row][col]=0
            else: A[row][col]=1
    return A

def randomCells(w,h):
    '''randomly assign 1s and 0s to places except outer edges'''
    A=createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row==0 or col==0 or row==h-1 or col==w-1: A[row][col]=0
            else: A[row][col]=random.choice([0,1])
    return A

def copy(A):
    '''deep copy array A into a new list of lists'''
    copy=createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            copy[row][col]=A[row][col]
    return copy

def innerReverse(A):
    '''creates a copy of A where all inner cells are reversed, and outer cells remain 0'''
    copy=createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row==0 or col==0 or row==len(A)-1 or col==len(A[0])-1: copy[row][col]=0
            elif A[row][col]==0: copy[row][col]=1
            else: copy[row][col]=0
    return copy

def countNeighbors(row,col, A):
    '''returns the numebr of neighbors of a cell'''
    neighbors = 0
    if A[row+1][col] == 1: neighbors += 1
    if A[row][col+1] == 1: neighbors += 1
    if A[row-1][col] == 1: neighbors += 1
    if A[row][col-1] == 1: neighbors += 1
    if A[row+1][col+1] == 1: neighbors += 1
    if A[row-1][col-1] == 1: neighbors += 1
    if A[row-1][col+1] == 1: neighbors += 1
    if A[row+1][col-1] == 1: neighbors += 1
    return neighbors

def next_life_generation(A):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0."""
    newA = createBoard(len(A[0]),len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row == 0 or row == (len(A) - 1) or col == 0 or col == (len(A[0]) - 1):
                A[row][col] = 0
            elif countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]  
    return newA
