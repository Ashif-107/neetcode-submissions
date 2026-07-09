class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        path = []

        def dfs(index):
            if index == len(digits):
                res.append("".join(path))
                return
                
            for c in keys[digits[index]]:
                path.append(c)
                dfs(index + 1)
                path.pop()
        
        dfs(0)
        return res