class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        pac, atl = set(), set()

        def dfs(r,c, visited, prev_h):
            if r < 0 or r >= rows or c < 0  or c >= cols:
                return
            
            if grid[r][c] < prev_h:
                return
            
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            for dr,dc in dirs:
                dfs(r+dr,c+dc, visited, grid[r][c])

        for r in range(rows):
            dfs(r,0,pac, grid[r][0])
            dfs(r,cols-1,atl, grid[r][cols-1])
        for c in range(cols):
            dfs(0,c,pac, grid[0][c])
            dfs(rows-1, c, atl, grid[rows-1][c])
        
        return list(pac & atl)