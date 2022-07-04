# https://leetcode.com/problems/rotate-list/
'''
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

#############################################################################################
# linked list
# TC: O(n)
# SC: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # close linked list into a ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        
        # find new tail : (n - k % n - 1)th node
        # new head      : (n - k % n)th node
        new_tail = head
        new_tail_index = n - k % n - 1
        for i in range(new_tail_index):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        # break the ring
        new_tail.next = None
        return new_head
