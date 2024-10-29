class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if (len(grid) == 0):
            return 0
        rows = len(grid)
        cols = len(grid[0])
        numOfIslands = 0
        visit = set();
        def bfs(r, c):
            queue = collections.deque()
            visit.add((r,c))
            queue.append((r,c))

            while queue:
                row,col = queue.popleft()
                directions = [[0,1], [1,0], [-1,0], [0,-1]]

                for dr,dc in directions: 
                    r,c = row+dr, col+dc
                    if (r in range(rows) 
                        and c in range(cols) 
                        and (grid[r][c] == "1")
                        and (r,c) not in visit):
                        visit.add((r,c))
                        queue.append((r, c))
                
        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visit and grid[row][col] == "1":
                    bfs(row,col)
                    numOfIslands +=1
        return numOfIslands
                
                