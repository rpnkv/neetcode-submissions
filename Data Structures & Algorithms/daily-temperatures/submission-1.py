class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        
        stack:tuple[int,int] = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_i, prev_t = stack.pop()
                result[prev_i] = i - prev_i
            
            stack.append((i,temp))

        return result