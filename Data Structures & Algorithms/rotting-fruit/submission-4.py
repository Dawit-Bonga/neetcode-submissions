from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        q = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        



        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for u,v in directions:
                    nr, nc = r + u, c + v
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1
        
        return minutes if fresh == 0 else -1
                    

