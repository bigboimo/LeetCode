class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        #Small optimization using index only instead of storing both temp and idx
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                currIdx = stack.pop()
                res[currIdx] = i - currIdx

            stack.append(i)

        return res