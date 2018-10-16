class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for p in range(1, len(prices)):
            profit += max(prices[p] - prices[p - 1], 0)
        return profit
