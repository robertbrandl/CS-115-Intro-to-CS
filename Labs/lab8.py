# Robert Brandl
# I pledge my honor that I have abided by the Stevens Honor System.



# Demo of hmmm, the Harvey Mudd miniature machine
# D.Naumann 2015, rev Oct 2018

# When this file is loaded, it runs the program assigned
# to variable RunThis. Debug mode is controlled by 
# variable Mode. Read all the comments before trying it out.
# Remember to press F5 to run, after making changes.  

import sys
import importlib
# Also requires hmmmAssembler.py and hmmmSimulator.py to
# be available in the same directory as this file.


# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops

Example1 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # assign r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# Example2 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...

Example2 = """
00 read r1          # get # from user to r1
01 write r1         # print the value of r1
02 addn r1 1        # add 1 to r1
03 jumpn 01         # jump to line 01
04 halt             # never halts! [use ctrl-c]
"""

# AbsVal is a program that asks the user for
# an input and then prints its absolute value.

AbsVal = """
00 read r1
01 jltz r1 4     # if r1 < 0 go to line 4
02 write r1      # print the absolute value
03 halt
04 setn r2 -1
05 mul r1 r1 r2  # assign r1 = r1 * -1 
06 jumpn 2       # go to line 2  
"""

# StoreLoad is an example program that
#   1) asks the user for an input
#   2) stores the value in a memory location
#   3) increments it and stores in another location
#   4) loads from that location and writes that value
# Try changing 11 to the address of an instruction!

StoreLoad = """
00 read r1         
01 storen r1 11   # put the value into mem[11]
02 addn r1 1       
03 setn r2 13 
04 storer r1 r2   # put incremented value into mem[13]
05 loadn r1 13
06 write r1       # write what was loaded
07 halt
"""

Triangle1 = """
00 read  r1          # get base
01 read  r2          # get height
02 mul   r1 r1 r2    # b times h into r1
03 setn  r2 2
04 div   r1 r1 r2    # divide by 2
05 write r1
06 halt
"""

Factorial = """
# Input: n 
# Assume: n >= 0
# Output: n!
#

# register usage: r1 for the input, r13 for the output

0       read    r1         # Get n
1       setn    r13 1      # initialize r13
2       jeqzn   r1 6       # done if r1 is 0
3       mul     r13 r13 r1 # change r13 = r13 * r1
4       addn    r1 -1      # change r1 = r1 - 1
5       jumpn   2          # repeat
6       write   r13
7       halt
"""

QUIZ = '''
00 read r1    #reads a number n to r1
01 addn r1 1  #adds 1 to n
02 setn r2 0  #sets r2 to 0
03 write r2   #write out r2
04 addn r2 1  #increments r2
05 addn r1 -1 #decrements r1
06 jgtzn r1 03#checks if r1 is greater than 0, if so go to line 3
07 halt       # stops program
'''

Exponent = '''
# Input n k, assume n>=0, k>=0, Output n**k

00 read r1
01 setn r13 1
02 read r2
03 jeqzn r2 07
04 mul r13 r13 r1
05 addn r2 -1
06 jumpn 03
07 write r13
08 halt
'''

fibonacci = '''
00 read r1      #reads in a number n, representing the number of digits of the fibonacci sequence to be printed
01 setn r2 1    #sets r2 equal to 1
02 setn r3 0    #sets r3 equal to 0
03 jeqzn r1 10  #checks whether the base case is 0 (no output) and determines when the process will end
04 write r3     #prints out the value in r3 (the value in the fibonacci sequence)
05 addn r1 -1   #decrements the n value (r1)
06 copy r4 r2   #copies the current value of r2 into r4
07 add r2 r2 r3 #changes the r2 value to r2+r3
08 copy r3 r4   #copies the value of r4 into r3
09 jumpn 03     #jumps back to the check statement in line 3
10 halt         #ends the program
'''
# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = fibonacci

# Choose whether to use debug mode; uncomment one of the following lines.
# Mode = ['-n'] # not debug mode, 
Mode = ['-d'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b


