class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numRows, numCols = len(board), len(board[0])

        def convertToY(row,col):
            if (row < 0 or col < 0 
            or row >= numRows or col >= numCols 
            or board[row][col] != "O"):
                return
            
            board[row][col] = "Y"
            convertToY(row+1, col)
            convertToY(row-1, col)
            convertToY(row, col+1)
            convertToY(row, col-1)

        for r in range(numRows):
            for c in range(numCols):
                if (r in [0, numRows -1] or c in [0, numCols -1]):
                    convertToY(r,c)
        for r in range(numRows):
            for c in range(numCols):
                if (board[r][c] == "O"):
                    board[r][c] = "X"
                if (board[r][c] == "Y"):
                    board[r][c] = "O"

    
