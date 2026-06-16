class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        l1 = l2 = 0
        mer = []
        while l1 < n and l2 < m:
            if nums1[l1] < nums2[l2]:
                mer.append(nums1[l1])
                l1 += 1
            elif nums2[l2] < nums1[l1]:
                mer.append(nums2[l2])
                l2 += 1
            else:
                mer.append(nums1[l1])
                l1 += 1
        
        while l1<n:
            mer.append(nums1[l1])
            l1 += 1
        while l2<m:
            mer.append(nums2[l2])
            l2 += 1 

        print(mer)

        total = n + m
        if total % 2 == 1:
            return float(mer[total // 2])
        else:
            mid = total // 2
            return (mer[mid - 1] + mer[mid]) / 2.0