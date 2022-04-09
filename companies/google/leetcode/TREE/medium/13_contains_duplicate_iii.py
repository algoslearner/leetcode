'''
Given an integer array nums and two integers k and t, 
return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1
'''

###########################################################################################################
# BRUTE FORCE: Linear search (TLE)
# TC: O(N^2) = O(N * min(k,n))
# SC: O(1)
# Brute force solution is use two loops and test both the conditions. 
# The inner loop starts from i+1 to i+k. 
# Because of that, we no longer need to test one of the conditions since that is taken care of automatically.

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        for i in range(0, len(nums)):
            for j in range(i+1, i+k+1):
                if j < len(nums):
                    if abs(nums[i]-nums[j]) <= t:
                        return True
        return False
      
      
###########################################################################################################
# BINARY SEARCH TREE
# TC: O(n log (min(n,k))
# SC: O(min(n,k))

'''
Binary Search Tree Solution

Maintain a BST of previous k elements. This is the invariant for this problem!
When you get element x, we want to find an element y in the BST such that (y-x)<=t or (x-y)<=t
How do we find (y-x)<=t ? Solution: Find the smallest value in the BST greater than or equal to x i.e. ceiling of x. Then test that value for the above condition.If the smallest value greater than x doesnt meet the criterion, then no other value y greater than x will meet the condition. One may consider the smallest element y that is greater or equal to x as the successor of x in the BST, as in: "What is the next greater value of x?"
How do we find (x-y)<=t? Find the greatest element y in the BST which is smaller than or equal to x. Again if this y doesnt meet the condition, no other y in the BST will meet the condition. We consider the greatest element y that is smaller or equal to x as the predecessor of x in the BST, as in: "What is the previous smaller value of x?
Visualize or imagine this as x and its two closest neighbors.
After trying the above tests, if they fail, then put x in set
If the size of the set is larger than k, remove the oldest item - this maintains the invariant.
Time complexity : O(n * log (min(n,k))). Space complexity: O(min(n,k))
'''

###########################################################################################################
# BINARY SEARCH TREE
# TC: O(n)
# SC: O(n)

'''
Buckets Method
Maintain buckets each of size t+1 holding the last k elements. This is the invariant.
Buckets are [0, t], [t+1,2t+1], [2t+2, 3t+2],....
What are the conditions of a match? Either x lies in a bucket which already has a member (this directly means that x and this element are within t of each other). Or the two neighbors of around this bucket may have a potential match. Check the code for an explanation.
Lastly we notice how we purge elements from the cache/buckets which are stale i.e. outside the window of k elements.
Notice one more thing: -3//5 = -1 - Python does this automatically and hence we dont need any special magic for handling negative numbers.
'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False
        cache = {}
        for i in range(len(nums)):
            if i-k > 0:
                bucket_id_to_delete = nums[i-k-1]//(t+1)
                del cache[bucket_id_to_delete]
            bucket_id = nums[i]//(t+1)
            condition1 = (bucket_id in cache)
            condition2 = ((bucket_id-1 in cache and abs(cache[bucket_id-1]-nums[i])<= t))
            condition3 = ((bucket_id+1 in cache and abs(cache[bucket_id+1]-nums[i])<= t))
            if condition1 or condition2 or condition3:
                return True
            cache[bucket_id] = nums[i]
        return False

