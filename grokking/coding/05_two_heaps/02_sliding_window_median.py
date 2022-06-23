#
'''
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[ 1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0
Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0
'''

######################################################################################################################
# two heaps
# TC: O(N.K), where N is the number of elements in array and K is size of sliding window
# SC: O(K)

from heapq import *
import heapq

class Solution:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
    
    def rebalance_heaps(self):
        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))
    
    def remove(self, heap, element):
        i = heap.index(element)
        
        heap[i] = heap[-1]
        del heap[-1]
        
        if i < len(heap):
            heapq._siftup(heap, i)
            heapq._siftdown(heap, 0, i)
        
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = [0.0 for _ in range(len(nums)- k + 1)]
        
        for i in range(len(nums)):
            if not self.maxheap or nums[i] <= -self.maxheap[0]:
                heappush(self.maxheap, -nums[i])
            else:
                heappush(self.minheap, nums[i])
            self.rebalance_heaps()
            
            # if we have k elements in sliding window, find median
            if i - k + 1 >= 0:
                if len(self.maxheap) == len(self.minheap):
                    median = (-self.maxheap[0] + self.minheap) / 2.0
                    result[i - k + 1] = median
                else:
                    result[i - k + 1] = -self.maxheap[0] / 1.0
            
            # remove elements going out of sliding window
            elementToBeRemoved = nums[i - k + 1]
            if elementToBeRemoved <= -self.maxheap[0]:
                self.remove(self.maxheap, -elementToBeRemoved)
            else:
                self.remove(self.minheap, elementToBeRemoved)
            self.rebalance_heaps()
        
        return result
            
                
            
