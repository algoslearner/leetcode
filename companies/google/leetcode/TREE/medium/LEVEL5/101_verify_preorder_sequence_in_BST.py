# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
'''
255. Verify Preorder Sequence in Binary Search Tree

Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

 

Example 1:


Input: preorder = [5,2,1,3,6]
Output: true
Example 2:

Input: preorder = [5,2,6,1,3]
Output: false
 

Constraints:

1 <= preorder.length <= 104
1 <= preorder[i] <= 104
All the elements of preorder are unique.
 

Follow up: Could you do it using only constant space complexity?
'''

# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/discuss/68197/AC-Python-O(n)-time-O(1)-extra-space
##################################################################################################################
# preorder = root, left, right
# STACK
# TC: O(N)
# SC: O(N)

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower = float("-inf")
        for x in preorder:
            if x < lower: 
                return False
            
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
                
        return True
      
##################################################################################################################
# no extra space
# TC: O(N)
# SC: O(1)

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        i = 0
        lower = float("-inf")
        for x in preorder:
            if x < lower: 
                return False
            
            while i > 0 and x > preorder[i - 1]:
                lower = preorder[i - 1]
                i -= 1
            preorder[i] = x
            i += 1
            
        return True
