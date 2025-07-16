class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.left = None
        self.right = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.right = self.tail
        self.tail.left = self.head
    
    def remove(self, node):
        prev = node.left
        nxt = node.right
        prev.right = nxt
        nxt.left = prev
    
    def insert(self, node):
        nxt = self.head.right
        self.head.right = node
        node.left = self.head
        node.right = nxt
        nxt.left = node

    def get(self, key: int) -> int: 
        if key in self.cache.keys():
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                lru = self.tail.left
                self.remove(lru)
                del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)