class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1Counts = Counter(arr1)
        added = set()
        sortArr = []
        res = []


        for n in arr2:

            if n in arr1Counts and n not in added:
                res.extend([n] * arr1Counts[n])
            elif n not in added:
                sortArr.add(n)
            added.add(n)
            
        for n in arr1:
            if n in added:
                continue
            sortArr.append(n)

        print(res)
        print(sortArr)

        for n in sorted(sortArr):
            res.append(n)

        return res

        

