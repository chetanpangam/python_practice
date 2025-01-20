"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

"""
class LinkedListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, size):
        self.capacity = size
        self.count = 0
        self.cache = dict()
        self.head = LinkedListNode(0,0)
        self.tail = LinkedListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_at_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.delete_node(node)
            self.insert_at_head(node)
            return node.val
        return -1
    
    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.delete_node(node)
            self.insert_at_head(node)
            return
        
        if self.count >= self.capacity:
            delete_key = self.tail.prev.key
            node = self.cache[delete_key]
            self.delete_node(node)
            del self.cache[delete_key]

        new_node = LinkedListNode(key, val)
        self.cache[key] = new_node
        self.insert_at_head(new_node)
        self.count += 1


lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
print(lRUCache.get(1));    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2));    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1));    # return -1 (not found)
print(lRUCache.get(3));    # return 3
print(lRUCache.get(4));    # return 4
