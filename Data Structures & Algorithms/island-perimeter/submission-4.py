class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i,j):
            if not (0 <= i < rows and  0 <= j < cols) or grid[i][j] == 0:
                return 1
            
            if grid[i][j] == 2:
                return 0
            
            grid[i][j] = 2
            result = 0
            for u,v in directions:
                result += dfs(i + u, v + j)
            
            return result

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)


            
