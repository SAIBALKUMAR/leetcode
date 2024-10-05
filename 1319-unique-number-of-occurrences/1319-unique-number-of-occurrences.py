class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            if (i in hashmap):
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        newArr = hashmap.values()
        newHashmap = {}
        for i in newArr:
            if (i in newHashmap):
                return False
            else:
                newHashmap[i] = 1

        return True