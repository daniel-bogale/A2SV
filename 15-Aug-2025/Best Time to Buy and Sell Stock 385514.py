# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        max_profit = 0

        for selling_day in range(1, len(prices)):
            cheapest = min(cheapest, prices[selling_day])
            profit = prices[selling_day] - cheapest
            max_profit = max(max_profit, profit)

        return max_profit