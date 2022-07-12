"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""


class Solution(object):
    """Return max profit from days of stocks. Buy low, sell high!"""

    @staticmethod
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        low = prices[0]
        for price in prices:
            high = price
            profit = max(profit, high - low)
            low = min(low, high)
        return profit


if __name__ == "__main__":
    assert Solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert Solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution.maxProfit([1, 2]) == 1
    assert Solution.maxProfit([2, 1]) == 0
    assert Solution.maxProfit([1]) == 0
