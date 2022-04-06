'''
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#########################################################################################
# QUEUE
# TC: O(N)
# SC : O(N)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = deque([root])
        while q:
            size = len(q)
            
            # iterate over all nodes on current level
            for i in range(size):
                node = q.popleft()
                
                # check if next pointers are on same level
                if i < size - 1:
                    node.next = q[0]
                    
                # add the children to back of the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
      
#########################################################################################
# USE NEXT POINTERS
# TC: O(N)
# SC : O(1)

# pseudocode
'''
leftmost = root
 while (leftmost != null)
 {
     curr = leftmost
     prev = NULL
     while (curr != null)
     {
         → process left child
         → process right child
         → set leftmost for the next level
         curr = curr.next
     }
 }
 '''

class Solution:
    
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            if prev:
                prev.next = childNode
            else:    
                leftmost = childNode
            prev = childNode 
        return prev, leftmost
    
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if not root:
            return root
        
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next
        return root 
