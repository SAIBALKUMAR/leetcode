class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        left = 0
        right = price[-1] -1
        result = 0

        def checkMidForTastiness(mid):
            count = 1
            prev = price[0]
            for i in range(1, len(price)):
                if price[i]-prev >= mid:
                    count +=1
                    prev = price[i]
                if (count == k):
                    return True
            return False
            
        while left <=right:
            mid = (left + right) // 2
            if checkMidForTastiness(mid):
                left = mid +1 
                result = mid
            else:
                right = mid-1
        return result