class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        long = 0

        for n in nums:
            if n -1 not in s:
                l = 1
                curr = n
                while(curr+1) in s:
                    l += 1
                    curr += 1
                
                long = max(l, long)
        
        return long