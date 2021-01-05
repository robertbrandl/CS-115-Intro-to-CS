'''Robert Brandl'''
'''I pledge my honor that I have abided by the Stevens Honor System.'''

def change(amount, coins):
    '''returns a non-negative integer indicating the minimum number of coins required to make up the given amount (a non-negative integer)'''
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        useIt = min(1 + change(amount - coins[0], coins[1:]), 1 + change(amount - coins[0], coins))
        loseIt = change(amount, coins[1:])
        return min(useIt,loseIt)
