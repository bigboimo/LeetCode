class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        diff = 0
        sortedHeights = sorted(heights)
        for i in range(len(heights)):
            if sortedHeights[i] != heights[i]:
                diff += 1

        return diff
        