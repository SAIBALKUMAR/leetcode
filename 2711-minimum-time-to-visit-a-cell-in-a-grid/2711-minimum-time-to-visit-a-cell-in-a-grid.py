class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1],grid[1][0]) > 1:
            return -1 
        time = 0
        visit = set()
        ROWS,COLS = len(grid), len(grid[0])
        min_heap = []
        heapq.heappush(min_heap, (0,0,0))
        while min_heap:
            time, row, col = heapq.heappop(min_heap)

            if row == ROWS -1 and col == COLS-1:
                return time
            
            directions = [(row+1, col), (row-1,col), (row, col-1), (row, col+1)]

            for nr, nc in directions:
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in visit:
                    continue
                if (abs(grid[nr][nc] - time) % 2):
                    wait = 0
                else: 
                    wait = 1
                nc_time = max(grid[nr][nc] +  wait, time+1)
                heapq.heappush(min_heap, (nc_time, nr,nc))
                visit.add((nr,nc))
            

        

