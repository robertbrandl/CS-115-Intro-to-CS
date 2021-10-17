#Robert Brandl
#I pledge my honor that I have abided by the Stevens Honor System.
from cs115 import *
class Board (object):
    def __init__(self,width =7,height=6):
        '''initializes the board'''
        self.width = width
        self.height = height
        chars = []
        def addRow(L):
            for num in range(width):
                L += [' ']
            return L
        for num in range(height):
            chars += [addRow([])]
        self.chars = chars
    def __str__(self):
        '''returns a string representation'''
        s = ''
        for L in self.chars:
            s += '|'
            for ele in L:
                s += ele +"|"
            s += "\n"
        s+='-'
        for val in range(self.width*2):
            s +='-'
        s+='\n '
        for num in range(self.width):
            s += (str(num) + ' ')
        return s
    def allowsMove(self,col):
        '''checks if a move can be made at col'''
        if col >= 0 and col <self.width and self.chars[0][col] == ' ':
            return True
        return False
    def addMove(self,col,ox):
        '''adds a move into col'''
        x = -1
        count = 0
        for row in self.chars:
            if row[col] == ' ':
                x = count
            count +=1
        self.chars[x][col]=ox
    def setBoard(self, moveString):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'

        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            
    def delMove(self,col):
        '''removes the top checker from column col'''
        if self.chars[1][col] != ' ':
            self.chars[1][col] = ' '
            
    def winsFor(self,ox):
        '''checks if ox won'''
        for x in range(self.height):
            for y in range(self.width):
                try:
                    if (self.chars[x][y] == ox and self.chars[x+1][y+1] == ox and self.chars[x+2][y+2] == ox and self.chars[x+3][y+3] == ox): return True
                except: pass
        for x in range(self.height):
            for y in range(self.width):
                try:
                    if (self.chars[x][y] == ox and self.chars[x+1][y-1] == ox and self.chars[x+2][y-2] == ox and self.chars[x+3][y-3] == ox): return True
                except: pass
        for x in range(self.height):
            for y in range(self.width):
                try:
                    if (self.chars[x][y] == ox and self.chars[x+1][y] == ox and self.chars[x+2][y] == ox and self.chars[x+3][y] == ox): return True
                except: pass
        for x in range(self.height):
            for y in range(self.width):
                try:
                    if (self.chars[x][y] == ox and self.chars[x][y+1] == ox and self.chars[x][y+2] == ox and self.chars[x][y+3] == ox): return True
                except: pass
        return False
    
    def hostGame(self):
        '''plays game'''
        print("Welcome to Connect Four!")
        win = False
        while self.winsFor('X') == False and self.winsFor('O') == False:
            print(self)
            choice = int(input("X's choice: "))
            while self.allowsMove(choice) == False:
                choice = int(input("X's choice: "))
            self.addMove(choice,'X')
            print(self)
            if self.winsFor('X') == True: win = True
            if win == False:
                choice = int(input("O's choice: "))
                while self.allowsMove(choice) == False:
                    choice = int(input("O's choice: "))
                self.addMove(choice,'O')
        if self.winsFor('X') == True: print('X wins -- Congratulations!')
        else: print('O wins -- Congratulations!')
        print(self)
