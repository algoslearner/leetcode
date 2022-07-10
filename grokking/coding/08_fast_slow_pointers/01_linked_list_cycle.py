# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

################################################################################
# fast and slow pointers
# TC: O(N)
# SC: O(1)

class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next
    
def hasCycle(head):
  slow, fast = head, head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
    
  return False
    
