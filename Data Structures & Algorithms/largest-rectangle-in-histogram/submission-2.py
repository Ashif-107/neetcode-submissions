class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        heights = [0] + heights + [0]

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1

                maxarea = max(maxarea, h*w)
            
            stack.append(i)
        
        return maxarea