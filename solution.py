class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, t))
        
        return res
