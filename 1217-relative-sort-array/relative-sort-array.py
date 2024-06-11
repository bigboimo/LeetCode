class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def addNum(n, times,list):
            for i in range(times):
                list.append(n)
        
        arr1Counts = Counter(arr1)
        added = set()
        sortArr = []
        res = []


        for n in arr2:
            if n in arr1Counts and n not in added:
                addNum(n,arr1Counts[n], res)
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

        

