class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        preMin = prices[0]
        preMax = prices[0]
        maxProfit = 0
        for n in prices:
            if (n < preMin):
                preMin = n
                preMax = n
            if (n > preMax):
                preMax = n
            print(n, preMin, preMax, maxProfit, preMax-preMin)
            if (maxProfit < preMax-preMin):
                maxProfit = max(maxProfit, preMax-preMin)
                preMax = n
        return maxProfit
