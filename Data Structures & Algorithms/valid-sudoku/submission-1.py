class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        
        for i in range(len(b)):
            for j in range(len(b[0])):
                num = b[i][j]
                if num == '.': continue

                box_id = i//3 * 3 + j//3
                if(num in row[i] or num in col[j] or num in box[box_id]):
                    return False
                
                row[i].add(num)
                col[j].add(num)
                box[box_id].add(num)
        
        return True
