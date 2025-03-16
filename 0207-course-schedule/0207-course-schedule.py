class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}
        for i,j in prerequisites:
            preMap[i].append(j)
        visited = set()
        def dfs(value):
            if value in visited:
                return False
            if preMap[value] == []:
                return True
            
            visited.add(value)

            for j in preMap[value]:
                if not dfs(j): return False
            visited.remove(value)
            preMap[value] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True