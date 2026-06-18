class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, hei = stack.pop()

                area = hei* (i - idx)
                maxarea = max(area,maxarea)

                start = idx
            stack.append((start,h))
        for idx,height in stack:
            area = height * (len(heights) - idx)
            maxarea = max(maxarea, area)
            
        return maxarea