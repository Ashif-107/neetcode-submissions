class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        INT_MAX = 2147483647

        ans = 0
        
        while x:
            if ans > INT_MAX // 10:
                return 0

            digit = x % 10

            if ans > INT_MAX // 10 and digit > 7:
                return 0

            ans = ans*10 + digit
            x = x//10

        return sign*ans