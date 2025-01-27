class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        upper, lower = 0, len(matrix) - 1
        x = 0

        while upper <= lower:
            xMid = (upper + lower)//2
            if matrix[xMid][0] <= target <= matrix[xMid][-1]:
                x = xMid
                break
            elif matrix[xMid][0] > target:
                lower = xMid - 1
            else:
                upper = xMid + 1

        l, r = 0, len(matrix[-1]) - 1
        while l <= r:
            mid = (l + r)//2
            if matrix[x][mid] > target:
                r = mid - 1
            elif matrix[x][mid] < target:
                l = mid + 1
            else:
                return True
                
        return False

