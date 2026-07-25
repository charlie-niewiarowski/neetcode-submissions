# NOTES !!!!

'''
We can model this as a two dimensional array with,
    Row: representing a day
    Col: representing a state,
        0: We are not holding any stock
        1: We are holding some stock (maybe from today, maybe from tomorrow)
        2: We are selling today, and are in cooldown (lets calculate those sweet profits)

Therefore, we can model each day as a subproblem that answers the question...

--------------- What is the maximum I can make if this is the LAST day I'm trading -----------------

What are the actions we take at each step? ... 
    Col = 0:
        - The most we can have is whatever our profits were from yesterday or whatever we had by not owning stock yesterday
    Col = 1:
        - The most sensible decision is to either hold the stock we had yesterday, or buy some today.
        - Whichever is cheaper is the one we should buy
    Col = 2:
        - We just sold, so our profits are the expenses of owning the stock yesterday plus the price we get from selling today
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][0] = 0                
        dp[0][1] = -prices[0]      
        dp[0][2] = float('-inf')

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
            

        return max(dp[len(prices) - 1][0], dp[len(prices) - 1][2])




