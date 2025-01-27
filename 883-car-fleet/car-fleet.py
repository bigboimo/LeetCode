class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []
        hashPair = {}

        #Dictionary to pair the speeds before sorting
        for i in range(len(position)):
            hashPair[position[i]] = speed[i]

        position = sorted(position)

        #Times to get there for a fleet
        for i in range(len(position)):

            time = (target - position[i])/hashPair[position[i]]

            while stack and stack[-1] <= time:
                stack.pop()

            
            stack.append(time)

        return len(stack)
