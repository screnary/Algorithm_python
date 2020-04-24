"""
146 LRU 缓存机制
数据结构
进阶：O(1)时间复杂度的操作函数
"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        # capacity: int
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key):
        if key in self.dict:
            self.dict.move_to_end(key, last=True)
            return self.dict[key]
        else:
            return -1
    
    def put(self, key, value):
        if key in self.dict:
            self.dict.move_to_end(key, last=True)
        self.dict[key] = value
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)

class LRUCache_v2:
    def __init__(self, capacity):
        # capacity: int
        self.capacity = capacity
        self.dict = {}

    def get(self, key):
        if key not in self.dict:
            return -1
        value = self.dict.pop(key)
        self.dict[key] = value
        return value
    
    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        self.dict[key] = value
        if len(self.dict) > self.capacity:
            head = list(self.dict)[0]
            self.dict.pop(head)
