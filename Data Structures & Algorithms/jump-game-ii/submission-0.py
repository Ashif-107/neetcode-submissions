class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        curr_end = 0
        fart = 0

        for i in range(len(nums)-1):
            fart = max(fart, i+nums[i])

            if i == curr_end:
                count += 1
                curr_end = fart

        return count    
