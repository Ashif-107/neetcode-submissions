class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        summ = 0

        def dfs(index, summ, path):
            if summ == target:
                res.append(path[:])
                return
            
            if index == len(nums) or summ > target:
                return 

            path.append(nums[index])
            summ += nums[index]

            dfs(index, summ, path)
            summ -= path[-1]
            path.pop()
            dfs(index+1, summ, path)
        
        dfs(0,summ,path)

        return res