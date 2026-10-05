class new_node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.kv_dict = {}
        self.cap = capacity
        self.head = new_node(-1,-1)
        self.tail = new_node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):
        curr = node
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = curr.prev = None
    
    def add_before_tail(self,node):
        curr = node
        curr.prev = self.tail.prev
        curr.next = self.tail
        curr.prev.next = curr
        curr.next.prev = curr
    
    def get(self, key: int) -> int:
        if key in self.kv_dict:
            curr = self.kv_dict[key]
            self.remove(curr)
            self.add_before_tail(curr)
            return curr.val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv_dict:
            curr = self.kv_dict[key]
            curr.val = value
            self.remove(curr)
            self.add_before_tail(curr)
        else:
            if len(self.kv_dict) == self.cap:
                lru = self.head.next
                del self.kv_dict[lru.key]
                self.remove(lru)

            curr = new_node(key, value)
            self.add_before_tail(curr)
            self.kv_dict[key] = curr
                

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)