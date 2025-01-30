class TimeMap:

    def __init__(self):
        self.keyData = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyData[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        nums = self.keyData[key]
        l, r = 0, len(nums) - 1
        res = ""

        #Binary search to find number in logn
        while l <= r:
            mid = (l+r)//2
            currVal = nums[mid][1]

            
            if currVal <= timestamp:
                res = nums[mid][0]
                l = mid + 1
            elif currVal > timestamp:
                r = mid - 1
            else:
                return nums[mid][0]

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)