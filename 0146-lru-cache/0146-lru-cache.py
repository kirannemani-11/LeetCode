class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.right = self.tail
        self.tail.left = self.head
    
    def remove(self, node):
        prev = node.left
        nxt = node.right
        prev.right = nxt
        nxt.left = prev
    
    def insert(self, node):
        prev = self.tail.left
        prev.right = node
        node.left = prev
        node.right = self.tail
        self.tail.left = node

    def get(self, key: int) -> int:
        if key in self.hm.keys():
            node = self.hm[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            self.remove(node)
            newnode = Node(key,value)
            self.hm[key] = newnode
            self.insert(newnode)
        else:
            node = Node(key, value)
            self.hm[key] = node
            self.insert(node)
        if len(self.hm) > self.capacity:
            removal = self.head.right
            self.remove(removal)
            del self.hm[removal.key]   

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)