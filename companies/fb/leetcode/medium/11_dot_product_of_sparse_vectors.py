'''
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

 

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
'''

# ARRAY 
# TC : O(n)
# SC : O(1)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        length = len(self.nums)
        result = 0
        for i in range(length):
            result += self.nums[i] * vec.nums[i]
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

################################################
'''
I got this question at my FB onsite in August 2020. 
The interviewer did not accept my hashmap solution. 
He told me that hashing/lookups, while on surface look efficient, for large sparse vectors, 
hashing function takes up bulk of the computation that we might be better off with the first method. 
Wihile proposing hashmap/set solutions, take a minute to think about the complexity hashing function.

Update from recent FB onsite, interviewer didn't accept the HASHMAP solution and wanted to see the 2 pointers solution,
in addition he also came up with a follow up question, 
what would you do if one of the vectors werent fully "sparse" -> hint use binary search
'''


# TWO POINTER SOLUTION
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/discuss/1762961/Python-Dict-or-Two-Pointers
# Two Pointers (optimal solution):

class SparseVector:
    def __init__(self, nums: List[int]):
		'''
		T: O(N)
		S: O(L)
		'''
        self.non_zeros = []
        for i, n in enumerate(nums):
            if n != 0:
                self.non_zeros.append((i, n))
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
		'''
		T: O(min(L1, L2)) where L1 is length of self.non_zeros and L2 is length of vec.non_zeros
		S: O(L2), size of input?
		'''
        i, j, dot_prod = 0, 0, 0
		#only traverse the shorter pair list so the improvement is implicitly applied.
        while i < len(self.non_zeros) and j < len(vec.non_zeros): 
            if self.non_zeros[i][0] == vec.non_zeros[j][0]:
                dot_prod += self.non_zeros[i][1] * vec.non_zeros[j][1]
                i += 1
                j += 1
            elif self.non_zeros[i][0] < vec.non_zeros[j][0]:
                i += 1
            else:
                j += 1
        return dot_prod
