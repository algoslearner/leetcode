# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
####################################################################################
# brute force : go to end of list and count n backwards
# tc: O(n)
# sc: o(1)

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

	dummy = ListNode(0, head)
	prev = dummy
	curr = head

	# --- Go to end of List
	while curr:
		curr.prev = prev
		prev, curr = prev.next, curr.next

	# --- Reverse to (end - n)
	curr = prev
	for i in range(n):
		curr = curr.prev

	# --- Delete Node (end - n)
	curr.next = curr.next.next

	return dummy.next

####################################################################################
# two pointers
# tc: O(n)
# sc: o(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        
        for i in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        #removing Nth node from end
        slow.next = slow.next.next
        
        return head
