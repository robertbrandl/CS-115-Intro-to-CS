'''
Created on 10/7/2020
@author:   Robert Brandl
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 (Rev. Oct 2020 by D.N.)
'''
import turtle  # Needed for graphics

def sv_tree(trunk_length, levels):
    '''Draw a tree of integer trunk_length and of integer levels, using the turtle functions'''
    if levels == 0:
        return #
    else:
        turtle.forward(trunk_length)
        turtle.left(45)
        sv_tree (trunk_length / 2, levels - 1)
        turtle.right(45)
        turtle.backward(trunk_length)
        turtle.forward(trunk_length)
        turtle.right(45)
        sv_tree (trunk_length / 2, levels - 1)
        turtle.left(45)
        turtle.backward(trunk_length)

memo1 = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if (n) in memo1:
        return memo1[(n)]
    elif n < 0:
        return 0
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        answer = fast_lucas(n-1) + fast_lucas(n-2)
        memo1[(n)] = answer
        return answer

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        '''Does the job of fast_change, assuming coins is a tuple.'''
        if (amount,coins) in memo:
            return memo[(amount,coins)]
        elif amount == 0:
            return 0
        elif coins == ():
            return float("inf")
        elif coins[0] > amount:
            return fast_change_helper(amount, coins[1:], memo)
        else:
            useIt = min(1 + fast_change_helper(amount - coins[0], coins[1:], memo), 1 + fast_change_helper(amount - coins[0], coins, memo))
            loseIt = fast_change_helper(amount, coins[1:], memo)
            answer = min(useIt,loseIt)
            memo[(amount,coins)] = answer
            return answer

    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 7)
