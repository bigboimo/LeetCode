class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqNums = set(nums)
        longest = 0

        for n in seqNums:
            currLongest = 0
            if n - 1 not in seqNums: 
                while n + 1 in seqNums:
                    currLongest += 1 
                    n += 1
            longest = max(longest, currLongest + 1)

        return longest