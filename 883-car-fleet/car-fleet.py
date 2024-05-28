class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashPair = defaultdict(int)

        for i in range(len(position)):
            hashPair[position[i]] = speed[i]
        
        position = sorted(position)
        stack = []
        stack.append((target - position[-1]) / hashPair.get(position[-1]))

        for i in reversed(range(len(position))):
            if stack and stack[-1] < (target - position[i]) / hashPair.get(position[i]):
                stack.append( (target - position[i]) / hashPair.get(position[i]) )

        return len(stack)
