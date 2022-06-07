'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

##################################################################################################################
# Heap
# TC: O(N log k)
# SC: O(N+k)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
    
        freqmap = {}
        for i in nums:
            freqmap[i] = freqmap.get(i,0) + 1
        
        # return heapq.nlargest(k, freqmap.keys(), key = freqmap.get)
        
        # If we use a max heap, will it not be 0(N + KlogN)? N for heapify and KLogN for popping K times.
        minHeap = []
        for n, freq in freqmap.items():
            heapq.heappush(minHeap,(freq,n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        topNumbers = []
        while minHeap:
            topNumbers.append(heapq.heappop(minHeap)[1])
        return topNumbers


######################################################################################################
# Bucket sort
# https://leetcode.com/problems/top-k-frequent-elements/discuss/704226/Bucketsort-heaps-collections-QuickSelect-Solutions-with-Time-complexities
# TC: O(N)
# SC: O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
     
        for num, freq in Count: 
            bucket[-freq].append(num) 
        # return list(itertools.chain(*buckets))[:k]
        
        # flat_list = [item for sublist in bucket for item in sublist]
        flat_list = []
        for sublist in bucket:
            for item in sublist:
                flat_list.append(item)
        return flat_list[:k]

       
###############################################################################################################
# https://leetcode.com/problems/top-k-frequent-elements/solution/
# Quick select algorithm
# TC: O(N)
# SC: O(N)

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  
            
            return store_index
        
        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            # base case: the list contains only one element
            if left == right: 
                return
            
            # select a random pivot_index
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)
         
        n = len(unique) 
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.  
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]
