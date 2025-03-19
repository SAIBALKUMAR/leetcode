class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1 )]
        rank = [1] * (len(edges) +1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)

            if (parent1 == parent2):
                return False

            if rank[parent1] > rank[parent2]:
                rank[parent1] += rank[parent2]
                parent[parent2] = parent1
            else:
                rank[parent2] += rank[parent1]
                parent[parent1] = parent2
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
            