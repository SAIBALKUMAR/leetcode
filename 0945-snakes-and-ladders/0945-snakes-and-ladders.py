class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        lenBoard = len(board)
        board.reverse()
        def intToPos(square):
            r = (square - 1) // lenBoard
            c = (square - 1) % lenBoard
            if r%2:
                c = lenBoard - 1 -c
            return [r,c]
        que = deque()
        que.append([1,0])
        visit = set()

        while que:
            square,moves = que.popleft()

            for i in range(1,7):
                nextSquare = square + i
                r,c = intToPos(nextSquare)
                if (board[r][c] != -1):
                    nextSquare = board[r][c]
                if (nextSquare == lenBoard*lenBoard):
                    return moves + 1
                if (nextSquare not in visit):
                    que.append((nextSquare, moves +1))
                    visit.add(nextSquare)
        return -1
