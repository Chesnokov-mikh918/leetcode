class Node:
    def __init__(self, key=None, val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = dict()

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key not in self.cache_dict.keys():
            return -1
        node_target = self.cache_dict[key]
        self.remove(node_target)
        self.add_front(node_target)
        return node_target.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict.keys():
            node_target = self.cache_dict[key]
            node_target.val = value
            self.remove(node_target)
            self.add_front(node_target)

        elif len(self.cache_dict) < self.capacity:
            new_node = Node(key, value)
            self.add_front(new_node)
            self.cache_dict[key] = new_node
        
        else:
            oldest_node = self.tail.prev
            del self.cache_dict[oldest_node.key]
            self.remove(oldest_node)

            new_node = Node(key, value)
            self.add_front(new_node)
            self.cache_dict[key] = new_node
        


        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)