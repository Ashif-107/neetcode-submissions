class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        heights = [0] + heights + [0]
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                he = heights[stack.pop()]
                w = i - stack[-1] - 1

                maxarea = max(maxarea, he*w)
            
            stack.append(i)
        return maxarea