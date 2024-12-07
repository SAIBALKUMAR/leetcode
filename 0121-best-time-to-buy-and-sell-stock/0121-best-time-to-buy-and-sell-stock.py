class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        preMin = prices[0]
        maxProfit = 0
        for n in prices:
            if (n < preMin):
                preMin = n
            if (maxProfit < n-preMin):
                maxProfit = max(maxProfit, n-preMin)
        return maxProfit