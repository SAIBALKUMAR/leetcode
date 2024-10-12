class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # [13,5,1,8,21,2]
        # maxTaste = 10**9, maxArray=[]
        # getMaxArray
        # 
        if (len(price) < k):
            return 0
        price.sort()

        def fulfill(t):
            count = 1
            lastprice = price[0]
            for i in range(1, len(price)):
                if (price[i] - lastprice >= t):
                    count += 1
                    lastprice = price[i]
            return count >= k

        low, high = 0, price[-1] - price[0]
        while high > low:
            mid = high - (high - low) // 2
            if fulfill(mid):
                low = mid
            else:
                high = mid - 1 

        return low
