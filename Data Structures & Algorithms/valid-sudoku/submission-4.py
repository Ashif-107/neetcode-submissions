class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                b = (i // 3) * 3 + (j // 3) 
                num = board[i][j]

                if num in rows[i] or num in cols[j] or num in boxs[b]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxs[b].add(num)
        
        return True