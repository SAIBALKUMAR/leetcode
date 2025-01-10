class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) ==1 and len(matrix[0]) == 1:
            return int(matrix[0][0])
        cache = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        maxLength = 0;
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (int(matrix[i][j]) == 1):
                    cache[i][j] = 1 + min(int(cache[i-1][j-1]), int(cache[i][j-1]), int(cache[i-1][j]))
                    maxLength = max(maxLength, cache[i][j])
        
        return maxLength*maxLength


                    
