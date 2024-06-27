class Node():
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.cache = {}

        #Setting up doubly linked list
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def add(self, node):
        #Linking node before mru to this new node
        prev = self.mru.prev
        prev.next = node
        #Linking mru to node
        self.mru.prev = node
        #Linking node to prev and mru
        node.next = self.mru
        node.prev = prev

    def remove(self, node):
        #getting previous and next node
        prev = node.prev
        nxt = node.next
        #skipping over current not with pointers to remove it
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            #Bring node forward to mru
            self.remove(node)
            self.add(node)
            
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #If key is present, remove it from linked list and hashmap. 
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        #If we go over capacity, remove lest recent node from linked list and hashmap
        if len(self.cache) > self.cap:
            removeNode = self.lru.next
            del self.cache[removeNode.key]
            self.remove(removeNode)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)