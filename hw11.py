#Robert Brandl
#I pledge my honor that I have abided by the Stevens Honor System.
# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)
from cs115 import *

def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:
            print('Congratulations, you won!')
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:
            print('The computer has won')
            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    while num_piles <=0:
        num_piles = int(input("How many piles do you want to play with? "))
    piles = [0] * num_piles
    for pile in range(num_piles):
        while piles[pile] <= 0 :
            try:
                piles[pile] = int(input("What initial value do you want in pile " + str(pile) + "? "))
            except ValueError:
                continue

        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles
    num = 0
    for value in piles:
        print("pile " + str(num) + " = " + str(value))
        num+=1


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles
    pile = -1
    while pile < 0 or pile > (num_piles -1):
        pile = int(input("Which pile would you like to remove from? "))
        while pile >= 0 and pile <= num_piles - 1 and piles[pile] == 0:
            pile = int(input("No coins left in this pile. Which pile would you like to remove from? "))
    return pile


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    remove = -1
    while remove <1 or remove > piles[pnum]:
        remove = int(input("How many would you like to remove from pile " + str(pnum) + "? "))
    return remove

def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles
    return reduce(lambda x,y: x^y,piles)

def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 
    nimsum = game_nim_sum()
    tup = ()
    for num in range(num_piles):
        if piles[num]^nimsum <piles[num] and piles[num]-piles[num]^nimsum == piles[num]:
            tup = (num,piles[num]-piles[num]^nimsum)
        elif piles[num]^nimsum <piles[num] and piles[num]-piles[num]^nimsum < piles[num]:
            tup = (num,piles[num]-piles[num]^nimsum)
    if tup == ():
        for num in range(num_piles):
            if piles[num] > 0:
                tup = (num,1)
    return tup
    


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles
    opt = opt_play()
    piles[opt[0]]=piles[opt[0]]-opt[1]
    print("The computer removed " + str(opt[1])+ " from pile " + str(opt[0]))

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
