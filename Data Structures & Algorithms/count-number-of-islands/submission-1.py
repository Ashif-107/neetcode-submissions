class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if grid[r][c] != '1':
                return
            
            grid[r][c] = '0'
            
            for dr,dc in dirs:
                dfs(r+dr, c+dc)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        
        return count