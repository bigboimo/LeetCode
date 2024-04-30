class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Merge sort implementation
        def mergeSort(string, s, e):
            if s >= e:
                return string

            mid = (s + e)//2

            mergeSort(string, s, mid)
            mergeSort(string, mid + 1, e)
            merge(string, s, mid, e)

            return string
        
        def merge(string, start, mid, end):
            left = string[start : mid + 1]
            right = string[mid + 1 : end + 1]
            l, r = 0, 0
            k = start

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    string[k] = left[l]
                    l += 1
                else: 
                    string[k] = right[r]
                    r += 1
                k += 1
            
            while l < len(left):
                string[k] = left[l]
                l += 1
                k += 1
            
            while r < len(right):
                string[k] = right[r]
                r += 1
                k += 1

        lString = [x for x in s]
        rString = [y for y in t]

        print(lString)
        print(rString)

        first = mergeSort(lString, 0, len(lString))
        second = mergeSort(rString, 0, len(rString))

        print(first)
        print(second)

        return "".join(first) == "".join(second)
            