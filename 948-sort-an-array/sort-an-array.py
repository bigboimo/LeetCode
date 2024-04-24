class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr, start, end):
            if start >= end:
                return arr
            
            mid = (start + end)//2
            #First half of array split
            mergeSort(arr, start, mid)
            #Second half of array split
            mergeSort(arr, mid + 1, end)
            #Merge the subarrays
            merge(arr, start, mid, end)
            #Return the sorted array after the merging is done
            return arr
        
        def merge(arr, start, mid, end):
            left, right = arr[start : mid + 1], arr[mid + 1 : end + 1]
            l, r, k = 0, 0 , start

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    arr[k] = left[l]
                    l += 1
                else:
                    arr[k] = right[r]
                    r += 1
                k += 1
            
            while l < len(left):
                arr[k] = left[l]
                l += 1
                k += 1
            
            while r < len(right):
                arr[k] = right[r]
                r += 1
                k += 1
            
        return mergeSort(nums, 0, len(nums))
