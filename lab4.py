'''Robert Brandl'''
'''I pledge my honor that I have abided by the Stevens Honor System.'''

def knapsack(capacity, itemList):
    ''' returns both the maximum value and the list of items that make this value, without exceeding
the capacity of your knapsack'''
    if itemList==[] or capacity==0:
        return [0,[]]
    elif itemList[0][0]>capacity:
        return knapsack(capacity,itemList[1:])
    useit=knapsack(capacity-itemList[0][0],itemList[1:])
    loseit=knapsack(capacity,itemList[1:])
    if itemList[0][1]+useit[0]>loseit[0]:
        return [itemList[0][1]+useit[0],[itemList[0]]+useit[1]]
    return loseit
