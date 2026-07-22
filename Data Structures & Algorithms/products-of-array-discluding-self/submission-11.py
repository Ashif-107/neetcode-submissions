class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0]*n
        post = [0]*n

        pre[0] = 1
        post[n-1] = 1

        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            post[j] = post[j+1]*nums[j+1]

        res = []
        for i in range(n):
            res.append(pre[i]*post[i])
        
        return res