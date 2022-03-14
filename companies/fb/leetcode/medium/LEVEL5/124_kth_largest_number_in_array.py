'''
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

 

Example 1:

Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".
Example 2:

Input: nums = ["2","21","12","1"], k = 3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".
Example 3:

Input: nums = ["0","0"], k = 2
Output: "0"
Explanation:
The numbers in nums sorted in non-decreasing order are ["0","0"].
The 2nd largest integer in nums is "0".
 

Constraints:

1 <= k <= nums.length <= 104
1 <= nums[i].length <= 100
nums[i] consists of only digits.
nums[i] will not have any leading zeros.
'''

###############################################################################
# Approach 1 -- sorting O(NlogN)

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return sorted(nums, key=int)[-k]

#################################################################################
# Approach 2 -- priority queue O(NlogK)

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        pq = [] # min-heap 
        for x in nums: 
            heappush(pq, int(x))
            if len(pq) > k: heappop(pq)
        return str(pq[0])
      
      
################################################################################
# Approach 3 -- quick select

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(x) for x in nums]
        shuffle(nums)
        
        def part(lo, hi): 
            """Return partition of nums[lo:hi]."""
            i, j = lo+1, hi-1
            while i <= j: 
                if nums[i] < nums[lo]: i += 1
                elif nums[lo] < nums[j]: j -= 1
                else: 
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[lo], nums[j] = nums[j], nums[lo]
            return j 
        
        lo, hi = 0, len(nums)
        while lo < hi: 
            mid = part(lo, hi)
            if mid == len(nums)-k: return str(nums[mid])
            elif mid < len(nums)-k: lo = mid + 1
            else: hi = mid
