class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)

        for i in range(len(temps)):
            while stack and temps[i] > temps[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res
                