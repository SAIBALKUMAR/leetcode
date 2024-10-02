class Solution:
    def partitionString(self, s: str) -> int:
        partitions = []
        visited = ""
        j=0
        k=0
        for i in range(len(s)):
            if (s[i] in visited):
                partitions.append(s[j:i])
                j = i
                visited = ""
            visited += s[i]
        if (len(visited)>0):
            partitions.append(s[i:])
        return len(partitions)