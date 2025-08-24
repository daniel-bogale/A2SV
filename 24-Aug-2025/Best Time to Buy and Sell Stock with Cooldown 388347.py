# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dp(cur_day, holding):
            if cur_day >= len(prices):
                return 0

            if (cur_day, holding) in memo:
                return memo[(cur_day, holding)]
            
            max_profit = dp(cur_day + 1, holding)

            if not holding:
                max_profit = max(max_profit, dp(cur_day + 1, 1) - prices[cur_day])
            
            else:
                max_profit = max(max_profit, dp(cur_day + 2, 0) + prices[cur_day])
            
            memo[(cur_day, holding)] = max_profit
            return max_profit


        return dp(0,0)