class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        win_start = 0

        i = 1
        while (i < len(prices)):
            prof = prices[i] - prices[win_start]
            if prof < 0:
                win_start = i
            if prof > max_profit:
                max_profit = prof
            i += 1

        return max_profit 