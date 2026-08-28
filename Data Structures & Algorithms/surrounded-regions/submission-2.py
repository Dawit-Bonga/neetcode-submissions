from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque([])

        for c in range(cols):
            if board[rows - 1][c] == "O":
                board[rows - 1][c] = "D"
                q.append((rows - 1, c))
            if board[0][c] == "O":
                board[0][c] = "D"
                q.append((0, c))
        
        for r in range(rows):
            if board[r][cols - 1] == "O":
                board[r][cols - 1] = "D"
                q.append((r, cols - 1))
            if board[r][0] == "O":
                board[r][0] = "D"
                q.append((r, 0))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            i,j = q.popleft()
            for u,v in directions:
                nr, nc = i + u, j + v
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "D"
                    q.append((nr,nc))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "D":
                    board[i][j] = "O"


