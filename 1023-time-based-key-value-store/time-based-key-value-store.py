class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = self.hashmap[key]
        maxStr = ""

        l, r = 0, len(res) - 1

        while l <= r:
            mid = (l+r)//2
            
            if res[mid][1] <= timestamp:
                maxStr = res[mid][0]
                l = mid + 1
            else:
                r = mid - 1

            
       #
                
        return maxStr


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)