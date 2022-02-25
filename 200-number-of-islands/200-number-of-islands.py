class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        def check(grid,i,j):
            if i<0 or j<0 or j>=len(grid[0]) or i>=len(grid) or grid[i][j]!='1':
                return 
            grid[i][j]='2'
            res = check(grid,i+1,j) or check(grid,i-1,j) or check(grid,i,j+1) or check(grid,i,j-1)
            return res
            
            
        islands=0
        rows=len(grid)
        cols=len(grid[0])
        for  row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1' :
                    check(grid,row,col)
                    islands+=1
        return islands


