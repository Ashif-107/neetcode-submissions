class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        memo = {}

        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if j == m:
                return 1
            
            if i == n:
                return 0
                
            ans = 0
            if s[i] == t[j]:
                ans += dp(i+1,j) + dp(i+1,j+1)
            else:
                ans += dp(i+1,j)
            
            memo[(i,j)] = ans
            return ans
        
        return dp(0,0)