class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                index, tempp = stack.pop()
                days = i-index
                result[index] = days
        
            stack.append((i,temp))
        
        return result