class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = { c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)
        visit, cycle = set(), set()
        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereqMap[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if (dfs(crs) == False):
                return []
        return output


            
            

            
