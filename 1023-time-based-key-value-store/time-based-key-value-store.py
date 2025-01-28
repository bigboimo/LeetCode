class TimeMap:

    def __init__(self):
        self.keyVals = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyVals[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyVals:
            return ""

        nums = self.keyVals[key]
        l, r = 0, len(nums) - 1
        maxTimestamp = timestamp
        resStr = ""

        while l <= r:
            mid = (l+r) // 2                

            if nums[mid][1] <= timestamp:
                resStr = nums[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return resStr   


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)