class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newList = strs
        counter = defaultdict(list)

        for i in range(len(newList)):
            counter[tuple(sorted(newList[i]))].append(i)

        print(counter)

        res = counter.values()
        print(res)
        ret = []
        
        for nums in res:
            adds = []
            for n in nums:
                adds.append(strs[n])
            ret.append(adds)

        print(ret)
        return ret

        

      

