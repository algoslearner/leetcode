# https://leetcode.com/problems/copy-list-with-random-pointer/
'''
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. 
The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# we can modify 'random' field instead of the 'next' field in the copied list:

############################################################################################
# recursive
# tc: O(N)
# sc: O(N)

class Solution:
    def __init__(self):
        self.visited = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        if head in self.visited:
            return self.visited[head]
        
        # create new node
        node = Node(head.val, None, None)
        self.visited[head] = node
        
        # recursive copy
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
      
############################################################################################
# iterative with extra space
# tc: O(N)
# sc: O(N)

class Solution:
    def __init__(self):
        self.visited = {}
    
    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        old_node = head
        # create new head node
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node
        
        # iterate the linked list until all nodes are cloned
        while old_node:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            
            # move one step ahead in linked list
            old_node = old_node.next
            new_node = new_node.next
            
        return self.visited[head]
      
      
############################################################################################
# iterative with no extra space
# tc: O(N)
# sc: O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# we can modify 'random' field instead of the 'next' field in the copied list:

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        ptr = head
        while ptr:
            # cloned node
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
            
        # unweave the linked list
        ptr_old_list = head
        ptr_new_list = head.next
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
