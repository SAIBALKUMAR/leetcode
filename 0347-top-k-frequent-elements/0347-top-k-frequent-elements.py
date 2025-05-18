class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]
        result = []
        for num in nums:
            count[num] += 1
        for num,cnt in count.items():
            freq[cnt].append(num)
        
        for i in range(len(freq)-1, 0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result