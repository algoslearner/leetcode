# https://leetcode.com/problems/remove-linked-list-elements/
'''
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

########################################################################################
# ITERATIVE
# TC: O(n)
# SC: O(1)

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            if curr.val == val:
                if prev and head:
                    prev.next = curr.next
                    curr.next = None
                    curr = prev.next
                else:
                    head = head.next
                    curr = head
            else:
                prev = curr
                curr = curr.next
                
        return head
      
########################################################################################
# RECURSION
# TC: O(n)
# SC: O(n)

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def rec(node, val):
            if node:
                if node.val == val:
                    return rec(node.next, val)
                else:
                    node.next = rec(node.next, val)
                return node
        return rec(head, val)
