class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # set borders as allowed
        # go to the first non-border cell with left right top and bottom 
        # do dfs on all four sides such that we find allowed 1, other wise set not allowed and set visited true
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        land, borderland = 0,0
        def dfs(row, col):
            if (row,col) in visited or row > ROWS -1  or col > COLS -1 or row< 0 or col <0 or (not grid[row][col]):
                return 0                
            visited.add((row,col))
            res = 1 
            redirect = [[0,1], [1,0], [-1, 0], [0, -1]]
            for i,j in redirect:
                res += dfs(row+i, col+j)
            return res

        for i in range(ROWS):
            for j in range(COLS):
                land += grid[i][j]
                if (grid[i][j] and (i in [0, ROWS-1] or j in [0, COLS-1] )):
                    borderland += dfs(i,j)
        return land - borderland