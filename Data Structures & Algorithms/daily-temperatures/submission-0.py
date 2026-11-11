class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            
            stack.append(i)
            
        return res