class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        l = len(nums)
        res = []
        nums.sort()
        
        for i in range(l-2):
            if i>0 and nums[i] == nums[i-1]:
                continue 
            j = i+1
            k = l-1

            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])

                    j+=1
                    k-=1

                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                
                if nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                if nums[i]+nums[j]+nums[k] > 0:
                    k -= 1


        return res