# 
'''
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example 1:

1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
'''

#################################################################################################################################################
# two heaps - minheap and maxheap
# TC: O(log N) for insert
# SC: O(N)

from heapq import *

class MedianOfAStream:
  def __init__(self):
    self.minheap = []
    self.maxheap = []

  def insert_num(self, num):
    if not self.maxheap or -self.maxheap[0] >= num:
      heappush(self.maxheap, -num)
    else:
      heappush(self.minheap, num)

    # maintain length
    if len(self.maxheap) > len(self.minheap) + 1:
      heappush(self.minheap, -heappop(self.maxheap))
    elif len(self.maxheap) < len(self.minheap):
      heappush(self.maxheap, -heappop(self.minheap))

  def find_median(self):
    if len(self.maxheap) == len(self.minheap):
      return (-self.maxheap[0] + self.minheap[0]) / 2.0
    return -self.maxheap[0] / 1.0


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()

'''
Output 0.74s

The median is: 2.0
The median is: 3.0
The median is: 3.5
'''
