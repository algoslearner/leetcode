#
'''
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
'''

#####################################################################################################
# minheap
# TC: O(N log k)
# SC: O(k)

from heapq import *

class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

def merge_lists(lists):
  minheap = []

  for root in lists:
    if root:
      heappush(minheap, root)

  resulthead = resultTail = None
  while minheap:
    node = heappop(minheap)
    if resulthead is None:
      resulthead = resultTail = node
    else:
      resultTail.next = node
      resultTail = resultTail.next

    if node.next:
      heappush(minheap, node.next)

  return resulthead
