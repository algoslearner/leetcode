# https://leetcode.com/problems/lfu-cache/
# amazon 8, linkedin 3, google 3
'''
460. LFU Cache

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
 

Constraints:

0 <= capacity <= 104
0 <= key <= 105
0 <= value <= 109
At most 2 * 105 calls will be made to get and put.
'''

#############################################################################################################
# https://leetcode.com/problems/lfu-cache/discuss/2086590/Python-solution-with-three-dict
'''
3 DICT
main idea:
using three map, key_to_value, key_to_freq, freq_to_keys to finish this implementation
in python 3 the dict will maintain the insertion order so can use it to implement the fuction of LinkedHashSet in java.
'''

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = collections.defaultdict(dict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        
        self.increase_freq(key)
        return self.key_to_val[key]    
        
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return -1
        
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self.increase_freq(key)
            return
        
        if self.capacity <= len(self.key_to_val):
            self.remove_min_freq_key()
        
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        
        self.freq_to_keys[1][key] = None
        
        self.min_freq = 1
        
    
    #update KF & FK table
    def increase_freq(self, key):
        if key not in self.key_to_freq:
            self.key_to_freq[key] = 1

        freq = self.key_to_freq[key]
        self.key_to_freq[key] = self.key_to_freq[key] + 1
            
        del self.freq_to_keys[freq][key]
        self.freq_to_keys[freq + 1][key] = None
        
        if len(self.freq_to_keys[freq]) == 0:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
    
    def remove_min_freq_key(self):
        
        keys = self.freq_to_keys[self.min_freq]
        key = next(iter(keys))
        
        del self.freq_to_keys[self.min_freq][key]

        if len(keys) == 0:
            del self.freq_to_keys[self.min_freq]
        
        del self.key_to_val[key]
        del self.key_to_freq[key]
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#######################################################################################################################
# DLL + 2 dict
# https://leetcode.com/problems/lfu-cache/discuss/1979424/Python%3A-DLL-%2B-2-Dictionaries-O(1)-solution

class Node:
    def __init__(self, key, val, frequency):
        self.val = val
        self.key = key
        self.frequency = frequency
        self.next = None
        self. prev = None
        
class DLL:
    def __init__(self):
        self.head = Node('#','#','#')
        self.tail = Node('/','/','/')
        self.head.next = self.tail
        self.tail.prev = self.head

class LFUCache:

    def __init__(self, capacity: int):
        self.frequencyMap = collections.defaultdict(DLL)
        self.leastFrequency = 1
        self.hashMap = {}
        self.capacity = capacity
        self.current = 0
        
    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        
        node = self.hashMap[key]
        freq = node.frequency
        
        self._remove(node)
        
        if self.frequencyMap[freq].head.next == self.frequencyMap[freq].tail:
            if self.leastFrequency == freq:
                self.leastFrequency += 1
        node.frequency += 1
        self._add(node.frequency, node)
        
        return node.val
    

    def put(self, key: int, value: int) -> None:
        if key not in self.hashMap:
            if self.current == self.capacity:
                node = self.frequencyMap[self.leastFrequency].tail.prev
                if node.val == '#':
                    return
                self.hashMap.pop(node.key)
                self._remove(node)
                self.current -= 1
            node = Node(key, value, 1)
            self.leastFrequency = 1
            self.hashMap[key] = node
            self._add(1, node)
            self.current += 1
        else:
            node = self.hashMap[key]
            node.val = value
            freq = node.frequency
            self._remove(node)
            if self.frequencyMap[freq].head.next == self.frequencyMap[freq].tail:
                if self.leastFrequency == freq:
                    self.leastFrequency += 1
            node.frequency += 1
            self._add(node.frequency, node)
            
    def _add(self, freq, node):
        head = self.frequencyMap[freq].head
        head.next.prev = node
        node.next = head.next
        node.prev = head
        head.next = node
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
