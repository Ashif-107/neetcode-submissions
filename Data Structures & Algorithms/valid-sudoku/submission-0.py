class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if b[i][j] == '.':
                    continue
                if (b[i][j] in rows[i] or
                    b[i][j] in cols[j] or
                    b[i][j] in box[(i//3,j//3)]
                    ):
                    return False
                
                cols[j].add(b[i][j])
                rows[i].add(b[i][j])
                box[(i//3,j//3)].add(b[i][j])

        return True