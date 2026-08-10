class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        memo = {}
        rows = len(matrix)
        cols = len(matrix[0])

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dp(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            
            leng = 1
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    leng = max(leng, 1+ dp(nr,nc))
            
            memo[(r,c)] = leng
            return leng
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dp(i,j)) 
        
        return ans

