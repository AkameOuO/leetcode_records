class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.table = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.tail.left = self.head
        self.head.right = self.tail

    def get(self, key: int) -> int:
        node = self.update(key)
        if node is None:
            return -1
        
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.update(key, value)
        if node is None:
            node = Node(key, value)
            self.push(node)
            if self.len > self.capacity:
                self.remove()
        # self.print()

    def update(self, key, val=None):
        if key not in self.table:
            return None
        
        node = self.table[key]
        
        self.remove(node)
        self.push(node)

        if val is not None:
            node.val = val
        
        return node
    
    def remove(self, node=None):
        if node is None:
            node = self.head.right
        l = node.left
        r = node.right
        l.right = r
        r.left = l
        node.right = None
        node.left = None
        del self.table[node.key]

        self.len -= 1
    
    def push(self, node):
        node.left = self.tail.left
        node.right = self.tail
        self.tail.left.right = node
        self.tail.left = node
        self.table[node.key] = node

        self.len += 1
    
    def print(self):
        node = self.head
        while node:
            print(node.val, end=" ")
            node = node.right
        print()



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)