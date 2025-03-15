class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge_count = [0] * n
        for n1, n2 in roads:
            edge_count[n1] +=1
            edge_count[n2] +=1
        result = 0
        label = 1
        for num in sorted(edge_count):
            result += num * label
            label +=1
        return result