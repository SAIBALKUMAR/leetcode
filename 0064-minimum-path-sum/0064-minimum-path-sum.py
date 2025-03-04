class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        result = [[float("inf")] * (COLS + 1) for j in range(ROWS + 1)]
        result[ROWS - 1][COLS] = 0
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1,-1, -1):
                result[r][c] = grid[r][c] + min(result[r+1][c], result[r][c+1])
        return result[0][0]
