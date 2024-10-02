class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        newRow = [0] * cols
        newRow[cols-1] = 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c]:
                    newRow[c] = 0
                elif c+1 < cols:
                    newRow[c] = newRow[c] + newRow[c+1]
        return newRow[0]
 