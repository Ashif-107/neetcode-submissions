class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        nums.sort()
        path = []

        def dfs(start, summ):
            if summ == target:
                res.append(path[:])
                return
            
            if summ > target:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
            
                path.append(nums[i])

                dfs(i + 1, summ+nums[i])

                path.pop()

        dfs(0,0)
        return res