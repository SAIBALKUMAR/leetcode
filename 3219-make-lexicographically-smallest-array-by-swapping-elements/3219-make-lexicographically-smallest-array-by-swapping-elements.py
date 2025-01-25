class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        res = []
        num_to_group = {}

        for n in sorted(nums):
            if not groups or abs(n-groups[-1][-1] > limit):
                groups.append(deque())
            groups[-1].append(n)
            num_to_group[n] = len(groups) -1 
        
        for n in nums:
            required_group = num_to_group[n]
            res.append(groups[required_group].popleft())
        
        return res
