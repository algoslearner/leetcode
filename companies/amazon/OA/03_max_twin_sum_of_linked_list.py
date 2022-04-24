'''
2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
'''

	"""
	You're guaranteed that the linked list will be even. If you try out some
	values for n, you'll see that at n = 0, the twin sum will be the last node..
	At n = 1, the twin node will be second to last node. And so on. 
	
	From there you can extract that you need to get the middle and reverse the first half.
	Once you do that, you can just traverse as normal from the middle node and the reverse start.
	"""
	# get middle and reverse first half
	# you could do two separate operations to get mid then reverse the first half until you reach the mid.
	# but that would be expensive since you'd traverse the first half twice so it's better to do it all in one go.

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev, slow, fast = None, head, head
        
        while fast and fast.next: # Setup for get mid logic
            fast = fast.next.next # Do this first so you avoid any issues with destructive operations when reversing the list.
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
         
		 # prev now points to the start of the reversed list
		 # slow now points to the middle of the list
        max_pair_sum = 0
        while prev and slow: # Simple loop to get the max pair sums
            pair_sum = slow.val + prev.val
            max_pair_sum = max(max_pair_sum, pair_sum)
            prev = prev.next
            slow = slow.next
        
        return max_pair_sum
