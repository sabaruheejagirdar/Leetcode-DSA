""" 
LEETCODE: 121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day 
in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example1
Input: prices = [7,1,5,3,6,4]
Output: 5

Example2
Input: prices = [7,6,4,3,1]
Output: 0
"""
"""
APPROACH:
left = BUY LOW;  right= SELL HIGH
1. Initialize Pointers: Set left to 0 and right to 1.
2. Track Minimum Price: Update left to right if prices[right] is lower than prices[left].
3. Calculate Profit: Compute the profit as prices[right] - prices[left] and update maxProfit if this profit is greater.
4. Iterate: Move right to the next position and repeat until the end of the list.
"""

def maxProfit(prices):   

    left, right = 0, 1
    maxProfit = 0

    while right < len(prices):
        # Keep track of minimum stock
        if prices[right] < prices[left]: 
            left = right

        maxProfit = max(maxProfit, prices[right] - prices[left])

        right += 1


    return maxProfit

prices = [7,6,4,3,1]
result = maxProfit(prices)
print(result)