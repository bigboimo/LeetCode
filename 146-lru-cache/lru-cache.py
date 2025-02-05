class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key) #Moves this node to Most Recently Used node
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        
        self.cache[key] = value

        #Checks if length of cache is longer than our capacity and pops the LRU node
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)