class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board),len(board[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(r,c,index):
            if index == len(word):
                return True

            if r< 0 or r >= n or c < 0 or c >= m or board[r][c] != word[index]:
                return False
            
            
            temp = board[r][c]
            board[r][c] = "#"

            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if dfs(nr,nc,index+1):
                    board[r][c] = temp
                    return True
            
            board[r][c] = temp
            return False
                

        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        
        return False