# https://leetcode.com/problems/all-oone-data-structure/
# linkedin 21, amazon 3, google 2, fb 2
'''
432. All O`one Data Structure

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
'''

######################################################################################################
# map, set, heap
# https://leetcode.com/problems/all-oone-data-structure/discuss/1610032/Python-accepted-simple-solution-with-explanation-or-Map-Set-Heap
# TC: (All methods): O(logn), where n is the unique keys in the Data Structure
# SC: O(m), where m is the number of calls made to the Data Structure.

class AllOne:

    def __init__(self):
        self.key_count = defaultdict(int)
        self.count_key = defaultdict(set)
        self.max_heap = []
        self.min_heap = []
        

    def inc(self, key: str) -> None:
        og_value = self.key_count[key]
        # If the value exists in the count map, we have to remove the key.
        if self.count_key[og_value]:
            self.count_key[og_value].remove(key)
        # Inc the value in the count map and key map 
        og_value+=1
        self.count_key[og_value].add(key)
        self.key_count[key]=og_value
        heapq.heappush(self.max_heap, -(og_value))
        heapq.heappush(self.min_heap, (og_value))   
        return
        

    def dec(self, key: str) -> None:
        og_value = self.key_count[key]
        # The value guaranteed exists in the count map (given), removing the key.
        self.count_key[og_value].remove(key)
        # Dec the value in the count map and key map 
        og_value -= 1
        # If the value has become 0, remove the key and return
        if og_value == 0:
            del self.key_count[key]
            return
        
        self.count_key[og_value].add(key)
        self.key_count[key]=og_value
        heapq.heappush(self.max_heap, -(og_value))
        heapq.heappush(self.min_heap, (og_value)) 
        return

    def getMaxKey(self) -> str:
        # The map keeps track of how many elements there are in the DS, so if its 
        # len is 0, we can just return back ""
        if len(self.key_count) == 0:
            return ""
        
        # We will keep popping values from the max heap and if the values exits in 
        # the count map, we add it back to the heap and return a key from the map.
        while self.max_heap:
            val = -heapq.heappop(self.max_heap)
            if self.count_key[val]:
                heapq.heappush(self.max_heap, -val)
                for key in self.count_key[val]:
                    return key
        return
        

    def getMinKey(self) -> str:
        if len(self.key_count) == 0:
            return ""
        
        # We will keep popping values from the min heap and if the values exits in 
        # the count map, we add it back to the heap and return a key from the map.
        while self.min_heap:
            val = heapq.heappop(self.min_heap)
            if self.count_key[val]:
                heapq.heappush(self.min_heap, val)
                for key in self.count_key[val]:
                    return key
        return

######################################################################################################
# doubly linked list
# https://leetcode.com/problems/all-oone-data-structure/discuss/91428/Python-solution-with-detailed-comments

from collections import defaultdict
class Node(object):
    def __init__(self):
        self.key_set = set([])
        self.prev, self.nxt = None, None 

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)        

    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None
    
    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList(object):
    def __init__(self):
        self.head_node, self.tail_node = Node(), Node()
        self.head_node.nxt, self.tail_node.prev = self.tail_node, self.head_node
        return

    def insert_after(self, x):
        node, temp = Node(), x.nxt
        x.nxt, node.prev = node, x
        node.nxt, temp.prev = temp, node
        return node
    
    def insert_before(self, x):
        return self.insert_after(x.prev)

    def remove(self, x):
        prev_node = x.prev
        prev_node.nxt, x.nxt.prev = x.nxt, prev_node
        return

    def get_head(self):
        return self.head_node.nxt
    
    def get_tail(self):
        return self.tail_node.prev

    def get_sentinel_head(self):
        return self.head_node

    def get_sentinel_tail(self):
        return self.tail_node
    
class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll, self.key_counter = DoubleLinkedList(), defaultdict(int)
        self.node_freq = {0:self.dll.get_sentinel_head()}

    def _rmv_key_pf_node(self, pf, key):
        node = self.node_freq[pf]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.node_freq.pop(pf)
        return

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.key_counter[key] += 1
        cf, pf = self.key_counter[key], self.key_counter[key]-1
        if cf not in self.node_freq:
            # No need to test if pf = 0 since frequency zero points to sentinel node
            self.node_freq[cf] = self.dll.insert_after(self.node_freq[pf])
        self.node_freq[cf].add_key(key)
        if pf > 0:
            self._rmv_key_pf_node(pf, key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.key_counter:
            self.key_counter[key] -= 1
            cf, pf = self.key_counter[key], self.key_counter[key]+1
            if self.key_counter[key] == 0:
                self.key_counter.pop(key)
            if cf != 0:
                if cf not in self.node_freq:
                    self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])
                self.node_freq[cf].add_key(key)
            self._rmv_key_pf_node(pf, key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() > 0 else ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.dll.get_head().get_any_key() if self.dll.get_tail().count() > 0 else ""

'''
Solution

All Oone Data Structure https://leetcode.com/problems/all-oone-data-structure/

Data-Structures
https://goo.gl/photos/YLhF2qCcBwRpAn58A

Node: A node type to support a doubly linked list. It is a container to hold a bag of keys. It supports:

add_key(key): Add a key to the bag
remove_key(key): Remove a key from the bag
get_any_key(): Returns any random key from the bag. Returns None if bag is empty.
is_empty(): Returns true if the bag is empty
DoubleLinkedList

The linked list is implemented using the idea of sentinel nodes, i.e. we have two dummy nodes to represent head and tail. Initially head.next points to tail and tail.prev points to head. Using two dummy nodes dramatically simplifies the implementation.
insert_after(x): Add a node after node x
insert_before(x): Add a node before node x
remove(x): Remove the node from the list
get_head(): Returns the reference to the real head node
get_tail() Returns the reference to the real tail node
node_freq: Hashmap with key as frequency and value as Node.
key_counter: Hashmap with key as input key and value as frequency of the key.

Algorithm Idea

A node in the doubly linked list represents a bucket containing a bag of words with a certain frequency. The doubly linked list is maintained in a sorted order with the head node containing words with the least frequency and the tail node containing words with maximum frequency.
Using this list, getMaxKey and getMinKey can be implemented in O(1) by returning any word contained in the tail and head respectively.
key_counter is hashmap which allows us to increment or decrement frequency of a key in O(1).
node_freq is a hashmap which maps a frequency integer to the bucket node in the linked list. Note that we initialize frequency 0 to head sentinel node.
Now, if we can maintain the sorted order of the linked list in O(1) while performing the increment and decrement operations, we would have a working solution!
Increment Details

While incrementing a key, we first update the key_counter ro reflect the new frequency (cf) of the key.
Then we test if there is already a bucket with cf using node_freq hashmap. If not, then we need to add a bucket to the linked list.
To maintain the sorted invariant, this new bucket must be after the bucket for frequency pf (cf-1).
Now unless pf is 0, we are guaranteed that a pf bucket already exists. Therefore, either we add the new bucket after the head node or after the pf bucket. Note that we initialize frequency 0 to head sentinel node. This allows us to use "insert_after" API when previous frequency were zero.
pf bucket can be retrieved in O(1) using node_freq. insertion in doubly linked list can be done in O(1) as well. Once we have inserted, we add the key to the new bucket.
Finally we need to remove the key from the previous bucket if pf > 0 (i.e. if a previous bucket exists). Again this can be done in O(1). If the previous bucket becomes empty after removing the key, then we need to also drop the entire bucket from the list.
Decrement Details

While decrementing a key, we first check if the key exisits in key_counter or not. If not, then we simply return. if it does exist, we update the key_counter to reflect the new frequency (cf) of the key. If cf is 0, then we drop this key from the key counter.
If cf is not in node_freq and cf is not 0, then we need to add a new bucket in the linked list such that the sorted invariant is maintained. Again we are guaranteed to have pf bucket!
We add the key to the new bucket and remove it from the previous bucket - O(1) operations.
'''
