class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        long = 0

        for n in nums:
            if n-1 not in s:
                len = 1
                cur = n
                while(cur+1) in s:
                    len += 1
                    cur += 1
                
                long = max(len,long)
        
        return long
            