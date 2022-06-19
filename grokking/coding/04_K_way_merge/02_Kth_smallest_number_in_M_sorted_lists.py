#
'''
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from 
the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
'''

####################################################################################
# minheap
# TC: O(K log M), M = total number of input arrays
# SC: O(M)

from heapq import *

def find_Kth_smallest(lists, k):
  minheap = []

  # put the first element of each list to minheap
  for i in range(len(lists)):
    heappush(minheap, (lists[i][0], 0, lists[i]))
  
  numberCount = number = 0
  while minheap:
    number, i, listparent = heappop(minheap)
    numberCount += 1
    if numberCount == k: break

    # if the array of the top element has more elements, add the next element to the heap
    if len(listparent) > i + 1:
      heappush(minheap, (listparent[i+1], i+1, listparent))

  return number

def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()

'''
Output
1.01s
Kth smallest number is: 4
'''
