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
    

######################################################################################## 
  # Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.
  # TC: O(N)
  # SC: O(1)
########################################################################################

def find_cycle_length(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:  # found the cycle
      return calculate_cycle_length(slow)

  return 0


def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length
