#
'''
Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:

The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
The class should expose a function add(int num) which will store the given number and return the Kth largest number.
Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.
'''

##################################################################################################
# minheap
# tc: O(log k) for add function
# sc: O(k)

from heapq import *

class KthLargestNumberInStream:
  minheap = []

  def __init__(self, nums, k):
    self.k = k
    for n in nums:
      self.add(n)
  
  def add(self, num):
    heappush(self.minheap, num)
    if len(self.minheap) > self.k:
      heappop(self.minheap)
    return self.minheap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()

'''
Output
0.81s
4th largest number is: 5
4th largest number is: 6
4th largest number is: 6
'''
