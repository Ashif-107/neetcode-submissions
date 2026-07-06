class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def steps(n):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]
            
            memo[n] = steps(n-1) + steps(n-2)
            return memo[n]

        return steps(n)