class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for num in nums:
            if(num - 1) not in s:
                i = 1
                while (num + i) in s:
                    i += 1
                ans = max(i,ans)
        

        return ans