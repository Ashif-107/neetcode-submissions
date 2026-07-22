class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0]*n
        prod = 1
        for i,num in enumerate(nums):
            pre[i] = prod*num
            prod *= num

        post = [0]*n
        pprod = 1
        for j in range(n-1,-1,-1):
            post[j] = pprod*nums[j]
            pprod *= nums[j]

        res = []
        for i in range(n):
            if i == 0:
                res.append(post[i+1])
                continue
            elif i == n-1:
                res.append(pre[i-1])
            else:   
                res.append(post[i+1] * pre[i-1])


        return res