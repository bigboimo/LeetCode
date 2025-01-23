class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longestSeq = 0

        for i in seq:
            currSeq = 0 
            if i - 1 not in seq: 
                first = i
                print(first)
                for j in range(len(seq)):
                    if first + 1 in seq:
                        currSeq += 1
                        first += 1
                    else:
                        break
            print(currSeq)
            longestSeq = max(longestSeq, currSeq + 1)
        
        return longestSeq
        