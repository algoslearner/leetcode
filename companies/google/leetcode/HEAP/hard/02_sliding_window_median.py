# https://leetcode.com/problems/sliding-window-median/
'''
480. Sliding Window Median

The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
 

Constraints:

1 <= k <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
'''

##########################################################################################################
# Two heaps

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
            
                
            
