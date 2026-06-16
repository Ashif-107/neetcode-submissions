class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                boxid = i//3 * 3 + j//3

                if board[i][j] == '.':
                    continue
                
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxs[boxid]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxs[boxid].add(board[i][j])
        
        return True