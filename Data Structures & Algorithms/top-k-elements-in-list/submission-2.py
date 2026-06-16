class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        l = [item for item,freq in count.most_common(k)]

        return l