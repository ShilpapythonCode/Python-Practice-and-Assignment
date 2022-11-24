'''2. This is a bonus question what kind of problem statements can be made but easy one.
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Input: prices = [7,1,5,3,6,4]
Output: 5
Note : Its an easy one just try to break the problem statement into smaller parts and then proceed.
'''

prices= [7,1,5,3,6,4]
def max_profit(prices):
#l=Buy Price and r=sell price
    l=0
    r=1
    profit_max=0

    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            profit_max=max(profit_max,profit)
        else:
            l+=1
        r+=1
    return profit_max
print(max_profit(prices))